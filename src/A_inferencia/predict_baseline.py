"""
FLUJO A1: Usar un Modelo Preentrenado del Hub

Este script descarga un modelo preentrenado y hace predicciones.

QUÉ APRENDES:
=============
- Cargar configuración desde YAML
- Descargar modelos del Hub
- Crear un pipeline (interfaz simple)
- Hacer predicciones

CONFIGURACIÓN NECESARIA:
========================
Archivo: configs/A_baseline.yaml
Contiene:
  - task: "sentiment-analysis"
  - model_id: "distilbert-base-uncased-finetuned-sst-2-english"
  - text: "ejemplo de texto"
  - cache_dir: "./outputs"

TAREAS A COMPLETAR:
===================
1. TODO: Importar librerías necesarias
   - dotenv.load_dotenv
   - transformers.pipeline
   - torch para detectar GPU
   - common.config.load_config (ya implementada)

2. TODO: Cargar configuración desde configs/A_baseline.yaml
   - config = load_config('configs/A_baseline.yaml')
   - Usar get_config_info(config) para mostrar
   - Campos esperados: task, model_id, text

3. TODO: Crear pipeline con los campos del YAML
   - task=config['task']
   - model=config['model_id']
   - device: 0 (GPU) o -1 (CPU)

4. TODO: Hacer predicción con config['text']
   - resultado = classifier(config['text'])

5. TODO: Mostrar resultados
   - label y score del resultado

USO:
====
python src/A_inferencia/predict_baseline.py
"""

import sys
import os
from pathlib import Path

# Agregar raíz del proyecto al path
sys.path.insert(0, os.path.abspath(os.path.join(Path(__file__).parent.parent.parent)))

from config import load_config, get_config_info
from dotenv import load_dotenv
from transformers import pipeline
import torch


if __name__ == "__main__":
    print("\n" + "="*60)
    print("🚀 FLUJO A1: Predicción con Modelo Preentrenado")
    print("="*60 + "\n")
    

    
    # TODO 2: Cargar variables de entorno desde .env
    load_dotenv()
    
    # TODO 3: Cargar configuración desde configs/A_baseline.yaml
    config = load_config('configs/A_baseline.yaml')
    get_config_info(config)

    task = config['task']
    model_id = config['model_id']
    text = config['text']   
    
    # TODO 4: Verificar GPU disponible
    device = 0 if torch.cuda.is_available() else -1
    print(f"Dispositivo: {'GPU 🔥' if device == 0 else 'CPU'}")
    
    # TODO 5: Crear pipeline (usa task y model_id del YAML)
    classifier = pipeline(task=task, model=model_id, device=device)
    
    # TODO 6: Hacer predicción (usa text del YAML)
    resultado = classifier(text)
    
    # TODO 7: Mostrar resultado (label y score)
    print(f"\n📝 Texto: {text}")
    print(f"🎯 Predicción: {resultado[0]['label']}")
    print(f"📊 Confianza: {resultado[0]['score']:.4f}\n")