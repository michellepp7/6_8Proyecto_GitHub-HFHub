# 📋 ENTREGA FINAL - Checklist y Validación

---

## 📝 CHECKLIST DE ENTREGA PARA ESTUDIANTES

### Cuentas Online
- [ ] Cuenta GitHub activa
- [ ] Cuenta Hugging Face Hub activa  
- [ ] Token HF generado (Write access)

### Repositorios Creados
- [ ] Repositorio GitHub: `6_8Proyecto_GitHub+HFHub`
- [ ] Repositorio Hugging Face Hub: `6_8Proyecto_GitHub+HFHub`

### Entorno Local
- [ ] Python 3.8+ instalado
- [ ] Entorno virtual `gpu_env` creado
- [ ] Dependencias instaladas (via setup_gpu_env.sh)
- [ ] Archivo `.env` configurado con token

### Flujo A - Baseline (Predicción)
- [ ] `python src/A_inferencia/predict_baseline.py` funciona
- [ ] Se carga modelo preentrenado del Hub
- [ ] Se hace predicción correctamente

### Flujo B - Entrenamiento
- [ ] `python src/B_finetuning/train_and_push.py` ejecutado
- [ ] Modelo entrenado por 1 época  
- [ ] Modelo publicado en tu Hub
- [ ] Archivos en Hub: `model.bin`, `config.json`, `tokenizer.json`

### Flujo A Parte 2 - Tu Modelo
- [ ] Configuración `A_finetuned.yaml` editada
- [ ] `python src/A_inferencia/predict_finetuned.py` funciona
- [ ] Descargas y usas TU modelo desde Hub

### Versionado GitHub
- [ ] Repositorio clonado
- [ ] Código pusheado a GitHub
- [ ] Commits con mensajes claros
- [ ] README visible en GitHub

### Reflexión Final
- [ ] Entiendo cómo funciona GitHub
- [ ] Entiendo cómo funciona Hugging Face Hub
- [ ] Puedo explicar el flujo completo
- [ ] Sé cómo usar un modelo preentrenado
- [ ] Sé cómo entrenar un modelo básico

---

## 💡 ERRORES COMUNES

| Error | Solución |
|-------|----------|
| `ModuleNotFoundError: transformers` | `bash setup_gpu_env.sh` |
| `HF_TOKEN not found` | Editar `.env` + agregar token |
| `CUDA out of memory` | Bajar `batch_size` en YAML |
| `Git not configured` | `git config --global user.email "test@example.com"` |
| `Permission denied` | `chmod +x setup_gpu_env.sh` |

---
