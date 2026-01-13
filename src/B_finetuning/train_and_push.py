"""
FLUJO B: Entrenar y Publicar Modelo

⚠️ IMPORTANTE: Este archivo es SOLO referencia.
Para entrenar, usa el notebook: notebooks/Flujo_B_FineTuning.ipynb

El notebook es MEJOR porque:
✅ Ves el progreso paso a paso
✅ Visualización de datos
✅ Métricas en tiempo real
✅ Debugging más fácil
✅ Puedes pausar y reanudar

EJECUTAR:
❌ NO: python src/B_finetuning/train_and_push.py
✅ SÍ: Abre notebooks/Flujo_B_FineTuning.ipynb

TIEMPO ESTIMADO:
================
- Con GPU RTX 4080: ~8 minutos (5000 ejemplos, 1 época)
- Con CPU: ~45 minutos

FLUJO COMPLETO:
===============
1. Flujo A (Baseline): predict_baseline.py
2. Flujo B (Entrenar): notebook Flujo_B_FineTuning.ipynb ← AQUÍ
3. Flujo A2 (Tu modelo): predict_finetuned.py

QUÉ APRENDES:
=============
- Cargar dataset (IMDb)
- Preparar datos para transformers
- Configurar entrenamiento (learning rate, epochs, etc)
- Entrenar modelo DistilBERT
- Publicar en Hugging Face Hub
- Que otros descarguen y usen tu modelo

CONFIGURACIÓN:
==============
Los parámetros vienen de configs/B_train.yaml:
- dataset_id: "imdb" (dataset a usar)
- base_model_id: "distilbert-base-uncased" (modelo a entrenar)
- num_train_epochs: 1 (número de épocas)
- learning_rate: 2e-5 (tasa de aprendizaje)
- per_device_train_batch_size: 16 (tamaño de batch)
- hf_repo_id: "TU_USUARIO_HF/6_8Proyecto_GitHub+HFHub" (dónde publicar)

CREDENCIALES NECESARIAS:
========================
En .env:
HF_TOKEN=hf_tu_token_aqui

Para obtener token: https://huggingface.co/settings/tokens

PRÓXIMOS PASOS:
===============
1. Abre el notebook: notebooks/Flujo_B_FineTuning.ipynb
2. Sigue las instrucciones paso a paso
3. Ejecuta cada celda (TODO)
4. Cuando termine, tu modelo estará en Hub
5. Ejecuta predict_finetuned.py para probarlo
"""

print(__doc__)
