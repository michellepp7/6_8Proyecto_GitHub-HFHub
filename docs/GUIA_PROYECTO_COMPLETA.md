# GUÍA COMPLETA DEL PROYECTO - Enunciado, Pasos y Configuración
---

## ENUNCIADO DEL PROYECTO

### Información General del Proyecto

**Nombre**: Proyecto GitHub + Hugging Face Hub  
**Modalidad**: Práctico (Hands-on)  
**Entrega**: Código en GitHub + Modelo en Hugging Face Hub  

---

### Contexto 

Este proyecto está diseñado para estudiantes que 

**¿Cuál es el propósito?**
- Aprender a usar **herramientas profesionales reales** (GitHub, Hugging Face Hub)
- Entender cómo se trabaja en la industria AI
- Ganar confianza al publicar un modelo entrenado
- Comprender el ciclo completo: Código → Entrenamiento → Publicación

**¿Qué SÍ aprenderás?**
- ✅ GitHub: crear repo, clonar, commits, push
- ✅ Hugging Face Hub: publicar modelos, compartir
- ✅ Workflow profesional: versionado + publicación
- ✅ Reutilización: usar modelos de otros
- ✅ Confianza en AI

---

###  Objetivo General

> **Crear un pipeline completo de ML que demuestre el ciclo profesional:**  
> **Código (GitHub) → Entrenamiento → Publicación (Hub) → Reutilización**

### 🔍 Objetivos Específicos

Al completar este proyecto, serás capaz de:

1. **Gestión de Versiones (GitHub)**
   - Crear un repositorio en GitHub
   - Clonar código de un repositorio remoto
   - Hacer commits con mensajes claros
   - Hacer push a GitHub
   - Documentar tu proyecto en README.md

2. **Publicación de Modelos (Hugging Face Hub)**
   - Crear un token de autenticación
   - Crear un repositorio de modelo en el Hub
   - Publicar modelos entrenados desde Python
   - Descargar y reutilizar modelos de otros

3. **Pipeline**
   - Cargar modelos preentrenados
   - Hacer predicciones (inferencia)
   - Entrenar un modelo con datos
   - Publicar modelo en la nube

4. **Pensamiento Profesional**
   - Entender por qué se versionan códigos
   - Comprender importancia de documentación
   - Valorar reproducibilidad
   - Trabajar de forma profesional

---

## 🎯 RECOMENDACIONES ESPECÍFICAS PARA ESTE PROYECTO

### 📊 Dataset Recomendado: **IMDb Sentiment Analysis**

```python
from datasets import load_dataset
dataset = load_dataset("imdb")
```

**Por qué IMDb:**
- ✅ **Lightweight**: 25K ejemplos (descargas rápidas)
- ✅ **Tarea clara**: Clasificación binaria (Positivo/Negativo)
- ✅ **Métricas obvias**: Accuracy, F1-Score fáciles de interpretar
- ✅ **Tiempo**: Fine-tuning ~8 min en GPU RTX 4080 (1 época)
- ✅ **Realista**: Verdadero problema de NLP

**Alternativas:**
- **AG News**: 120K ejemplos, 4 categorías (más ligero)
- **Custom Dataset**: Si tienes datos propios

---

### 🤖 Modelos Recomendados

#### **Flujo A - Predicción Baseline: DistilBERT** (RECOMENDADO)

```yaml
modelo: "distilbert-base-uncased-finetuned-sst-2-english"
tarea: "sentiment-analysis"
```

**Características:**
| Métrica | Valor |
|---------|-------|
| Parámetros | 67M (pequeño) |
| Tiempo predicción | ~3 segundos |
| Accuracy esperado | ~93% |
| Ventaja | Rápido y ligero |

**Alternativas:**
- `bert-base-uncased-finetuned-sst-2-english`: Más preciso (+2%) pero más lento
- `roberta-large-mnli`: Versátil pero muy pesado (355M parámetros)

---

#### **Flujo B - Fine-tuning: DistilBERT Base** (RECOMENDADO)

```yaml
modelo_base: "distilbert-base-uncased"
dataset: "imdb"
epochs: 1
batch_size: 16
learning_rate: 2e-5
```

**Características:**
| Métrica | Valor |
|---------|-------|
| Parámetros | 67M |
| Tiempo entrenamiento | ~8 min (GPU) |
| Accuracy esperado | 95-96% |
| Mejora vs Baseline | +2-3% |

**Configuración YAML Completa:**
```yaml
# B_train.yaml
model_name: "distilbert-base-uncased"
dataset_name: "imdb"
output_dir: "./outputs/distilbert-imdb"

training_args:
  num_train_epochs: 1
  per_device_train_batch_size: 16
  per_device_eval_batch_size: 32
  learning_rate: 2e-5
  weight_decay: 0.01
  warmup_steps: 100
  
push_to_hub: true
hub_model_id: "tu_usuario/6_8Proyecto_GitHub+HFHub"
```

---

#### **Flujo A Parte 2 - Tu Modelo Entrenado**

```yaml
# A_finetuned.yaml
modelo: "tu_usuario/6_8Proyecto_GitHub+HFHub"
cache_dir: "./outputs"
```

Descargarás automáticamente tu modelo desde Hub y harás predicciones.

---

### ⏱️ Tiempos Estimados (GPU RTX 4080)

| Paso | Tiempo | Nota |
|------|--------|------|
| Setup entorno | 5 min | Una sola vez |
| Flujo A (baseline) | 1 min | Predicción rápida |
| Flujo B (entrenamiento) | 8 min | 1 época IMDb |
| Flujo A Parte 2 | 1 min | Predicción con tu modelo |
| **Total** | **~15 min** | De inicio a modelo publicado |

---

### 📋 Checklist de Validación

Antes de empezar, verifica:

- [ ] GPU disponible: `nvidia-smi` (debe mostrar RTX 4080)
- [ ] PyTorch con CUDA: `python -c "import torch; print(torch.cuda.is_available())"`
- [ ] Token HF válido: `huggingface-cli login` (escribe `hf_xxxxx`)
- [ ] Dataset IMDb descargable: `python -c "from datasets import load_dataset; load_dataset('imdb')`

---

### 📊 Componentes del Proyecto

El proyecto se divide en **3 Flujos** que representan el ciclo completo:

#### **Flujo A: Predicción con Modelo Preentrenado** (Inferencia Inicial)

**Objetivo**: Entender cómo funcionan los modelos sin necesidad de entrenar

**Qué harás**:
- Descargar modelo preentrenado del Hub (`distilbert-base-uncased-finetuned-sst-2-english`)
- Hacer predicciones en análisis de sentimiento
- Entender flujo: Texto → Modelo → Predicción

**Resultado**: 
```
Input:  "I love this project!"
Output: POSITIVE (confianza: 0.999)
```

**Por qué es importante**: 
- Entiende que los modelos ya existen y están listos para usar
- No necesitas entrenar para hacer predicciones
- Muchos proyectos reutilizan modelos existentes

---

#### **Flujo B: Entrenamiento y Publicación** (El Núcleo)

**Objetivo**: Entrenar tu propio modelo y publicarlo profesionalmente

**Qué harás**:

1. **Descarga de Datos**
   - Descargar dataset SST2 (~8000 reseñas de películas)
   - Cada reseña tiene etiqueta: positiva o negativa

2. **Entrenamiento**
   - Cargar modelo base: `distilbert-base-uncased`
   - Entrenar con tus datos durante 1 época
   - Guardar modelo entrenado en `outputs/`

3. **Publicación**
   - Subir modelo a tu repositorio Hugging Face Hub
   - Publicar archivos: `model.bin`, `config.json`, `tokenizer.json`, `README.md`

**Resultado**: 
- Modelo en: `https://huggingface.co/tu_usuario/6_7Proyecto_GitHub+HFHub`
- Código en: `https://github.com/tu_usuario/6_7Proyecto_GitHub+HFHub`

**Por qué es importante**:
- Experimentas el ciclo completo profesional
- Aprendes a guardar y compartir modelos
- Otros pueden descargar y usar tu modelo

---

#### **Flujo A Parte 2: Predicción con Tu Modelo** (Reutilización)

**Objetivo**: Verificar que tu modelo funciona y entender reutilización

**Qué harás**:
- Descargar TU modelo que publicaste en Hub
- Hacer predicciones con tu modelo entrenado
- Comparar resultados con modelo preentrenado

**Resultado**: 
```
Input:  "This movie is amazing!"
Output: TU_MODELO predice POSITIVE
```

**Por qué es importante**:
- Verifica que publicación funcionó
- Entiende que modelos se pueden compartir y reutilizar
- Simula usar modelo de alguien más

---

###  Entregables Finales

Al terminar el proyecto, tendrás:

#### 1. **Repositorio en GitHub** ✅
```
https://github.com/tu_usuario/6_7Proyecto_GitHub+HFHub

Contiene:
├── src/ ...................... Scripts Python
├── configs/ ................... Configuración YAML
├── notebooks/ ................. Notebooks Jupyter
├── requirements.txt ........... Dependencias
├── setup_gpu_env.sh ........... Script setup
├── .gitignore ................. Archivos ignorados
└── README.md .................. Tu documentación
```

#### 2. **Modelo Publicado en Hub** ✅
```
https://huggingface.co/tu_usuario/6_7Proyecto_GitHub+HFHub

Contiene:
├── model.bin .................. Pesos del modelo
├── config.json ................ Configuración
├── tokenizer.json ............. Tokenizador
└── README.md .................. Documentación
```

#### 3. **Comprensión Demostrada** ✅
- Commits claros en GitHub
- Modelo funcionando en Hub
- README.md documentando el proyecto
- Ejecución exitosa de 10 pasos

---

### ✨ Criterios de Éxito

Habrás completado el proyecto exitosamente cuando:

- ✅ Repositorio GitHub existe y tiene código
- ✅ Commits con mensajes claros
- ✅ Modelo publicado en Hugging Face Hub
- ✅ `predict_baseline.py` funciona
- ✅ `train_and_push.py` se ejecutó
- ✅ `predict_finetuned.py` carga tu modelo
- ✅ README.md en raíz documentado
- ✅ Entiendes el flujo completo
- ✅ Puedes explicar qué aprendiste

##  PASOS DEL PROYECTO (10 pasos totales)

### PASO 0: Preparación - Crear Repositorios

**Qué hacer**:
1. Crear repositorio en GitHub
2. Crear repositorio en Hugging Face Hub
3. Generar token de HF

**Comando/URLs**:
- GitHub: https://github.com/new
- Hugging Face: https://huggingface.co/new
- Token HF: https://huggingface.co/settings/tokens

**Resultado esperado**:
```
✅ Repositorio GitHub: https://github.com/tu_usuario/6_7Proyecto_GitHub+HFHub
✅ Repositorio HF: https://huggingface.co/tu_usuario/6_7Proyecto_GitHub+HFHub
✅ Token: hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

### PASO 1: Setup - Configurar Entorno 

**Qué hacer**:
1. Navegar a carpeta del proyecto
2. Ejecutar script automático
3. Verificar instalación

**Comandos**:
```bash
# Navegar
cd 6_7Proyecto_GitHub+HFHub

# Setup automático (RECOMENDADO)
bash setup_gpu_env.sh

# O manual:
python -m venv gpu_env
source gpu_env/bin/activate  # Windows: gpu_env\Scripts\activate
pip install -r requirements.txt
```

**Configurar archivo .env**:
```bash
# Copiar template
cp .env.example .env

# Editar .env con tu token
nano .env
# Cambiar: HF_TOKEN=tu_token_aqui
```

**Resultado esperado**:
```
(gpu_env) tu_usuario@computer:~$ ✅ Entorno activo
✅ Dependencias instaladas
✅ .env configurado
```

---

### PASO 2: Estructura - Entender Proyecto 

**Qué hacer**:
Explorar carpetas y archivos

**Estructura**:
```
6_7Proyecto_GitHub+HFHub/
├── src/
│   ├── A_inferencia/
│   │   ├── predict_baseline.py .......... Predicción con modelo preentrenado
│   │   └── predict_finetuned.py ........ Predicción con tu modelo
│   ├── B_finetuning/
│   │   └── train_and_push.py ........... Entrenar y publicar
│   └── common/
│       ├── config.py ................... Cargar configuración
│       └── hf_auth.py .................. Autenticación HF

├── configs/
│   ├── A_baseline.yaml ................. Config Flujo A (preentrenado)
│   ├── B_train.yaml .................... Config Flujo B (entrenar)
│   └── A_finetuned.yaml ............... Config Flujo A (tu modelo)

├── notebooks/
│   ├── Flujo_A_Inferencia.ipynb ........ Template predicción
│   └── Flujo_B_FineTuning.ipynb ........ Template entrenamiento

├── data/ ............................ Datasets (creado auto)
├── outputs/ ......................... Modelos entrenados (creado auto)
├── requirements.txt ................. Dependencias Python
├── setup_gpu_env.sh ................. Script automático
└── .env ............................ Variables de entorno (NO compartir)
```

**Archivos Clave**:
| Archivo | Qué hace |
|---------|----------|
| `predict_baseline.py` | Carga modelo preentrenado y predice |
| `train_and_push.py` | Entrena modelo y lo publica |
| `predict_finetuned.py` | Carga tu modelo y predice |
| `*.yaml` | Configuración de parámetros |
| `.env` | Token y URLs (secreto) |

---

### PASO 3: Flujo A - Editar Configuración 

**Qué hacer**:
Editar archivo de configuración para predicción baseline

**Archivo**: `configs/A_baseline.yaml`

**Contenido original**:
```yaml
model_name: "distilbert-base-uncased-finetuned-sst-2-english"
task: "sentiment-analysis"
test_input: "I love this project!"
```

**Qué significa**:
- `model_name`: Modelo a descargar del Hub
- `task`: Tipo de tarea (análisis de sentimiento)
- `test_input`: Texto para predicción

**Puedes cambiar**:
- `test_input`: "Your text here"

**Resultado esperado**:
✅ Archivo guardado con cambios

---

### PASO 4: Flujo A - Ejecutar Predicción Baseline 

**Qué hacer**:
Ejecutar predicción con modelo preentrenado

**Comando**:
```bash
# Asegurar que entorno está activado
source gpu_env/bin/activate

# Ejecutar predicción
python src/A_inferencia/predict_baseline.py
```

**Qué pasa**:
1. Descarga modelo del Hub
2. Carga configuración
3. Hace predicción
4. Muestra resultado

**Resultado esperado**:
```
Texto: "I love this project!"
Predicción: POSITIVE (confianza: 0.999)
✅ Funciona!
```

**Si falla**:
- ❌ "ModuleNotFoundError": `bash setup_gpu_env.sh`
- ❌ "HF_TOKEN not found": Editar `.env`
- ❌ Conexión: Verificar internet

---

### PASO 5: Flujo B - Editar Configuración Entrenamiento 

**Qué hacer**:
Editar configuración para entrenar modelo

**Archivo**: `configs/B_train.yaml`

**Parámetros principales**:
```yaml
model_name: "distilbert-base-uncased"        # Modelo base
dataset_name: "sst2"                          # Dataset: 8000 ejemplos
num_epochs: 1                                 # 1 época = 10-15 min
batch_size: 8                                 # Procesa 8 textos a la vez
learning_rate: 2e-5                          # Velocidad aprendizaje
output_dir: "outputs"                        # Dónde guardar modelo
hf_repo_id: "tu_usuario/6_7Proyecto_GitHub+HFHub"  # CAMBIAR ESTO
```

**Configuración recomendada**:
- Para GPU: `num_epochs: 1`, `batch_size: 8`
- Para CPU: `num_epochs: 1`, `batch_size: 4`

**Archivo .env debe tener**:
```
HF_TOKEN=hf_tutoken_aqui
GITHUB_REPO=https://github.com/tu_usuario/6_7Proyecto_GitHub+HFHub
HF_REPO=https://huggingface.co/tu_usuario/6_7Proyecto_GitHub+HFHub
```

**Resultado esperado**:
✅ Configuración actualizada

---

### PASO 6: Flujo B - Entrenar Modelo 

**Qué hacer**:
Ejecutar entrenamiento. Este apartado no va a ser valorado, es preferible un peor resultado del modelo pero conseguir finalizar todos los pasos. 

**Comando**:
```bash
python src/B_finetuning/train_and_push.py
```

**Qué pasa** (en orden):
1. Verifica credenciales
2. Descarga dataset SST2 (~8000 ejemplos)
3. Carga modelo distilbert-base-uncased
4. **Entrena por 1 época** ← El paso más largo
5. Guarda modelo en `outputs/`
6. Sube a tu repositorio HF Hub

**Tiempo estimado**:
- GPU: 10-15 minutos
- CPU: 1-2 horas

**Output esperado**:
```
Loading dataset...
Training epoch 1/1... [████████████] 100%
Saving model to outputs/
Pushing to Hub...
✅ Model pushed to hub!
```

**Si falla**:
- ❌ "CUDA out of memory": Bajar `batch_size` en YAML
- ❌ "Connection error": Verificar token en `.env`
- ❌ "Authentication failed": Token inválido

---

### PASO 7: Verificar Modelo en Hub 

**Qué hacer**:
Confirmar que modelo está publicado

**URL**: 
```
https://huggingface.co/tu_usuario/6_7Proyecto_GitHub+HFHub
```

**Verificar que existe**:
- ✅ Repositorio visible
- ✅ Archivos: `model.bin`, `config.json`, `tokenizer.json`
- ✅ README.md

**Resultado esperado**:
```
✅ Tu modelo está publicado en Hub
✅ Cualquiera puede descargar y usar
```

---

### PASO 8: Flujo A Parte 2 - Usar Tu Modelo 

**Qué hacer**:
Configurar y ejecutar con tu modelo

**Archivo**: `configs/A_finetuned.yaml`

**Cambiar de**:
```yaml
model_name: "distilbert-base-uncased-finetuned-sst-2-english"
```

**A**:
```yaml
model_name: "tu_usuario/6_7Proyecto_GitHub+HFHub"
```

**Comando**:
```bash
python src/A_inferencia/predict_finetuned.py
```

**Qué pasa**:
1. Descarga TU modelo del Hub
2. Hace predicción con tu modelo
3. Muestra resultado

**Resultado esperado**:
```
Descargando modelo de: tu_usuario/6_7Proyecto_GitHub+HFHub
Texto: "This movie is amazing!"
Predicción: POSITIVE
✅ Tu modelo funciona!
```

---

### PASO 9: Versionado en GitHub 

**Qué hacer**:
Publicar código en GitHub

**Comandos**:
```bash
# Clonar repositorio
git clone https://github.com/tu_usuario/6_7Proyecto_GitHub+HFHub.git
cd 6_7Proyecto_GitHub+HFHub

# Configurar git
git config user.name "Tu Nombre"
git config user.email "tu@email.com"

# Copiar archivos
cp -r src/ configs/ notebooks/ .gitignore .env.example requirements.txt setup_gpu_env.sh .

# Hacer commits
git add .
git commit -m "Proyecto inicial: GitHub + Hugging Face Hub"
git branch -M main
git push -u origin main
```

**Verificar en GitHub**:
```
https://github.com/tu_usuario/6_7Proyecto_GitHub+HFHub
✅ Todos los archivos están allí
✅ .env NO está (seguridad)
```

---

### PASO 10: Validación Final 

**Qué hacer**:
Verificar que todo funciona

**Checklist**:
- [ ] `python src/A_inferencia/predict_baseline.py` funciona
- [ ] Hub tiene modelo publicado
- [ ] GitHub tiene código
- [ ] `python src/A_inferencia/predict_finetuned.py` funciona
- [ ] Entiendes GitHub → Hub flujo

**Resultado esperado**:
```
✅ Todo funciona
✅ Modelo publicado
✅ Código versionado
✅ ¡Proyecto completo!
```

---

##  CONFIGURACIÓN COMPLETA

### 1. Variables de Entorno (.env)

**Archivo**: `.env` (NUNCA compartir)

```ini
# Token de Hugging Face (de https://huggingface.co/settings/tokens)
HF_TOKEN=hf_tutoken_aqui

# URLs de tus repositorios
GITHUB_REPO=https://github.com/tu_usuario/6_7Proyecto_GitHub+HFHub
HF_REPO=https://huggingface.co/tu_usuario/6_7Proyecto_GitHub+HFHub
```

**Cómo obtener**:
- Token HF: https://huggingface.co/settings/tokens → "New token" → Copy
- GitHub URL: https://github.com/new → Copiar
- HF URL: https://huggingface.co/new → Copiar

---

### 2. Configuración YAML

#### A_baseline.yaml (Flujo A - Predicción Preentrenada)
```yaml
model_name: "distilbert-base-uncased-finetuned-sst-2-english"
task: "sentiment-analysis"
test_input: "I love this project!"
```

**Parámetros**:
- `model_name`: Modelo del Hub a usar
- `task`: Tipo de tarea
- `test_input`: Texto para predicción

**Modelos alternativos**:
- `"bert-base-uncased-finetuned-wnli"`
- `"distilbert-base-uncased"`

---

#### B_train.yaml (Flujo B - Entrenamiento)
```yaml
# Modelo
model_name: "distilbert-base-uncased"

# Dataset
dataset_name: "sst2"
num_train_samples: null  # null = todas

# Entrenamiento
num_epochs: 1
batch_size: 8
learning_rate: 2e-5
max_length: 128

# Guardado
output_dir: "outputs"
hf_repo_id: "tu_usuario/6_7Proyecto_GitHub+HFHub"

# Hardware
use_cuda: true  # false para CPU
```

**Qué significa cada parámetro**:
- `num_epochs`: Cuántas veces procesa el dataset (1 = 10-15 min)
- `batch_size`: Textos procesados a la vez (↓ menos memoria)
- `learning_rate`: Qué tan rápido aprende (2e-5 es estándar)
- `max_length`: Máximo de palabras por texto (128 = ~512 caracteres)

**Configuración para diferentes hardwares**:

GPU potente:
```yaml
batch_size: 16
num_epochs: 3
```

GPU modesta:
```yaml
batch_size: 8
num_epochs: 1
```

CPU:
```yaml
batch_size: 4
num_epochs: 1
use_cuda: false
```

---

#### A_finetuned.yaml (Flujo A - Tu Modelo)
```yaml
model_name: "tu_usuario/6_7Proyecto_GitHub+HFHub"
task: "sentiment-analysis"
test_input: "This is amazing!"
```

**Lo único que cambió**:
- `model_name`: Ahora es tu usuario/repositorio

---

### 3. Dependencies (requirements.txt)

```
transformers==4.36.2
torch==2.1.2
datasets==2.16.1
scikit-learn==1.3.2
PyYAML==6.0.1
huggingface_hub==0.20.2
python-dotenv==1.0.0
```

**Qué es cada uno**:
- `transformers`: Modelos PLN
- `torch`: Framework deep learning
- `datasets`: Descargar datasets públicos
- `scikit-learn`: Métricas y evaluación
- `PyYAML`: Leer archivos YAML
- `huggingface_hub`: Publicar en Hub
- `python-dotenv`: Cargar variables de entorno

---

### 4. Archivos Ignorados (.gitignore)

```
# Secretos (NUNCA compartir)
.env
*.env

# Datos (muy grandes)
data/
outputs/

# Entorno virtual
gpu_env/
venv/

# Python
__pycache__/
*.pyc
*.pyo

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
```

---

## 📋 CHECKLIST DE CONFIGURACIÓN

Antes de ejecutar, verifica:

- [ ] **Cuentas**:
  - [ ] GitHub account creada
  - [ ] HF account creada
  - [ ] Token HF generado

- [ ] **Repositorios**:
  - [ ] GitHub repo creado (vacío)
  - [ ] HF Hub repo creado (vacío)
  - [ ] Mismo nombre en ambos

- [ ] **Software**:
  - [ ] Python 3.8+ instalado
  - [ ] Git instalado
  - [ ] Conexión a internet

- [ ] **Archivo .env**:
  - [ ] `.env` existe
  - [ ] `HF_TOKEN=hf_...` completado
  - [ ] Rutas correctas

- [ ] **YAML configs**:
  - [ ] `A_baseline.yaml` revisado
  - [ ] `B_train.yaml` - hf_repo_id actualizado
  - [ ] `A_finetuned.yaml` - model_name actualizado

- [ ] **Hardware**:
  - [ ] GPU disponible (opcional, CPU también funciona)
  - [ ] 20GB disco libre (mínimo)
  - [ ] 8GB RAM (16GB recomendado)

---

## 🔧 TROUBLESHOOTING CONFIGURACIÓN

| Error | Causa | Solución |
|-------|-------|----------|
| `ModuleNotFoundError: transformers` | Dependencies no instaladas | `bash setup_gpu_env.sh` |
| `HF_TOKEN not found` | .env no configurado | Editar `.env` + agregar token |
| `CUDA out of memory` | batch_size muy grande | Bajar batch_size en YAML |
| `Permission denied setup_gpu_env.sh` | Script no ejecutable | `chmod +x setup_gpu_env.sh` |
| `Connection refused Hub` | Token inválido | Verificar token en `.env` |
| `FileNotFoundError: configs/B_train.yaml` | Ruta incorrecta | Ejecutar desde carpeta raíz |

---
