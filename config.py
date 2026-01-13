"""
Módulo de Configuración - Cargar YAML

Proporciona funciones para cargar archivos de configuración YAML.
Las configuraciones definen parámetros clave para cada Flujo:
- Flujo A (baseline): configs/A_baseline.yaml
- Flujo B (fine-tuning): configs/B_train.yaml
- Flujo A (custom): configs/A_finetuned.yaml

USO:
====
from config import load_config

config = load_config('configs/A_baseline.yaml')
model_id = config['model_id']
task = config['task']
"""

import yaml
from pathlib import Path
from typing import Dict, Any


def load_config(config_path: str) -> Dict[str, Any]:
    """
    Carga un archivo YAML de configuración.
    
    Args:
        config_path (str): Ruta al archivo YAML (relativa o absoluta)
        
    Returns:
        Dict[str, Any]: Diccionario con los parámetros de configuración
        
    Raises:
        FileNotFoundError: Si el archivo no existe
        yaml.YAMLError: Si hay error al parsear el YAML
        
    Ejemplo:
        >>> config = load_config('configs/A_baseline.yaml')
        >>> print(config['model_id'])
        'distilbert-base-uncased-finetuned-sst-2-english'
    """
    config_file = Path(config_path)
    
    # Verificar que el archivo existe
    if not config_file.exists():
        raise FileNotFoundError(
            f"❌ Archivo de configuración no encontrado: {config_path}\n"
            f"   Ubicación esperada: {config_file.absolute()}"
        )
    
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
            
        if config is None:
            raise ValueError(f"❌ El archivo YAML está vacío: {config_path}")
            
        return config
        
    except yaml.YAMLError as e:
        raise yaml.YAMLError(
            f"❌ Error al parsear YAML en {config_path}:\n{str(e)}"
        )


def validate_config(config: Dict[str, Any], required_keys: list) -> bool:
    """
    Valida que la configuración tenga todas las claves requeridas.
    
    Args:
        config (Dict): Configuración a validar
        required_keys (list): Lista de claves que deben existir
        
    Returns:
        bool: True si todas las claves existen
        
    Raises:
        ValueError: Si falta alguna clave requerida
        
    Ejemplo:
        >>> config = load_config('configs/A_baseline.yaml')
        >>> validate_config(config, ['model_id', 'task'])
        True
    """
    missing_keys = [key for key in required_keys if key not in config]
    
    if missing_keys:
        raise ValueError(
            f"❌ Configuración incompleta. Faltan campos: {missing_keys}"
        )
    
    return True


def get_config_info(config: Dict[str, Any]) -> str:
    """
    Retorna información legible de la configuración.
    
    Args:
        config (Dict): Configuración
        
    Returns:
        str: String con la información formateada
    """
    info = "📋 Configuración cargada:\n"
    for key, value in config.items():
        # No mostrar valores muy largos
        if isinstance(value, str) and len(value) > 50:
            value = value[:47] + "..."
        info += f"   {key}: {value}\n"
    return info
