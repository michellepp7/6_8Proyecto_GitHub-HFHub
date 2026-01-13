"""
FLUJO A2: Usar Tu Modelo Fine-tuneado del Hub

Este script carga TU MODELO ENTRENADO (en Flujo B)
y lo compara con el modelo baseline.

⚠️ IMPORTANTE:
Este script SOLO funciona después de Flujo B.
Tu modelo debe estar publicado en Hugging Face Hub.

CONFIGURACIÓN NECESARIA:
========================
Archivos: 
  - configs/A_baseline.yaml (modelo preentrenado)
  - configs/A_finetuned.yaml (TU modelo en Hub)

Campos esperados:
  - task: "sentiment-analysis"
  - model_id: "TU_USUARIO_HF/6_8Proyecto_GitHub+HFHub"
  - text: "ejemplo de texto"

Variable de entorno:
  - HF_TOKEN en .env (si el repo es privado)

TAREAS A COMPLETAR:
===================
1. TODO: Importar librerías necesarias
   - Mismo que predict_baseline.py
   - common.hf_auth.login_hf para autenticación

2. TODO: Cargar variables de entorno desde .env
   - load_dotenv()

3. TODO: Autenticarse en Hub (si es necesario)
   - login_hf() para obtener credenciales

4. TODO: Cargar ambas configuraciones
   - config_baseline = load_config('configs/A_baseline.yaml')
   - config_finetuned = load_config('configs/A_finetuned.yaml')
   - Maneja excepciones si A_finetuned no existe

5. TODO: Crear dos pipelines
   - classifier_baseline con config_baseline['model_id']
   - classifier_finetuned con config_finetuned['model_id']

6. TODO: Hacer predicciones con ambos
   - Usar config_baseline['text'] para ambos
   - Guardar resultados (label, score)

7. TODO: Comparar resultados
   - ¿Las predicciones son iguales?
   - Mostrar tabla comparativa

USO:
====
python src/A_inferencia/predict_finetuned.py

NOTA:
====
Solo funciona si Flujo B está completo y el modelo
está publicado en tu repositorio de HF Hub.
"""

import sys
import os
from pathlib import Path

# Agregar raíz del proyecto al path
sys.path.insert(0, os.path.abspath(os.path.join(Path(__file__).parent.parent.parent)))

from config import load_config, get_config_info
from hf_auth import login_hf


if __name__ == "__main__":
    print("\n" + "="*60)
    print("🚀 FLUJO A2: Predicción con Tu Modelo Fine-tuneado")
    print("="*60 + "\n")
    
    # TODO 1: Importar librerías necesarias
    pass
    
    # TODO 2: Cargar variables de entorno desde .env
    pass
    
    # TODO 3: Autenticarse en Hub (login_hf)
    pass
    
    # TODO 4: Cargar ambas configuraciones
    # - configs/A_baseline.yaml
    # - configs/A_finetuned.yaml (maneja error si no existe)
    pass
    
    # TODO 5: Crear dos pipelines
    # - Un para modelo baseline
    # - Otro para tu modelo (config_finetuned['model_id'])
    pass
    
    # TODO 6: Hacer predicciones con ambos modelos
    # - Usar el texto de config_baseline['text']
    pass
    
    # TODO 7: Comparar resultados
    # - ¿Son iguales las predicciones?
    # - Mostrar tabla: Baseline vs Tu Modelo
    pass
