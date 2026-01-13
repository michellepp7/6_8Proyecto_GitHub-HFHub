#!/bin/bash

# 🚀 SCRIPT DE INSTALACIÓN AUTOMATIZADA - FLUJO A+B GPU
# ======================================================
# Este script automatiza:
#   1. Crear entorno virtual gpu_env
#   2. Instalar todas las dependencias
#   3. Inicializar repositorio Git local
#   4. Crear repositorio en GitHub (opcional)
#   5. Crear dataset en Hugging Face Hub (opcional)
# Uso: bash setup_gpu_env.sh

# Para evitar salir por error en pasos opcionales, no usamos set -e

echo "=========================================="
echo "🚀 INSTALADOR COMPLETO - FLUJO A+B"
echo "   Proyecto: 6_7Proyecto_GitHub+HFHub"
echo "=========================================="
echo ""

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Variables
ENV_NAME="gpu_env"
PROJECT_NAME="6_7Proyecto_GitHub+HFHub"
REPO_NAME="6_7Proyecto_GitHub-HFHub"  # GitHub no permite + en nombres
WORK_DIR="$(pwd)"

echo -e "${BLUE}📍 Directorio de trabajo:${NC} $WORK_DIR"
echo -e "${BLUE}📦 Nombre del proyecto:${NC} $PROJECT_NAME"
echo ""

# ============================================
# PASO 1: Verificar Prerequisitos
# ============================================
echo -e "${YELLOW}[1/8] Verificando prerequisitos...${NC}"

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}✗ Python 3 no encontrado.${NC}"
    echo "Instala Python 3 primero: apt-get install python3 python3-venv"
    exit 1
fi
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo -e "${GREEN}✓ Python detectado: $PYTHON_VERSION${NC}"

# Verificar si hay GPU (opcional)
if command -v nvidia-smi &> /dev/null; then
    echo -e "${GREEN}✓ NVIDIA drivers detectados${NC}"
    echo -e "${BLUE}GPU detectada:${NC}"
    nvidia-smi -L
    HAS_GPU=true
else
    echo -e "${YELLOW}⚠ NVIDIA drivers no detectados (usará CPU)${NC}"
    HAS_GPU=false
fi

# Verificar Git
if ! command -v git &> /dev/null; then
    echo -e "${YELLOW}⚠ Git no detectado. Instálalo con: apt-get install git${NC}"
    HAS_GIT=false
else
    echo -e "${GREEN}✓ Git detectado${NC}"
    HAS_GIT=true
fi

echo ""

# ============================================
# PASO 2: Crear Entorno Virtual
# ============================================
echo -e "${YELLOW}[2/8] Creando entorno virtual $ENV_NAME...${NC}"

if [ -d "$ENV_NAME" ]; then
    echo -e "${YELLOW}⚠ El directorio '$ENV_NAME' ya existe${NC}"
    read -p "¿Deseas eliminarlo y crear uno nuevo? (s/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Ss]$ ]]; then
        rm -rf "$ENV_NAME"
        python3 -m venv "$ENV_NAME"
        echo -e "${GREEN}✓ Entorno virtual recreado${NC}"
    else
        echo -e "${GREEN}✓ Usando entorno existente${NC}"
    fi
else
    python3 -m venv "$ENV_NAME"
    echo -e "${GREEN}✓ Entorno virtual creado${NC}"
fi

# Activar entorno
source "$ENV_NAME/bin/activate"
echo -e "${GREEN}✓ Entorno activado${NC}"
echo ""

# ============================================
# PASO 3: Actualizar pip
# ============================================
echo -e "${YELLOW}[3/8] Actualizando pip, setuptools y wheel...${NC}"
pip install --upgrade pip setuptools wheel -q
echo -e "${GREEN}✓ Herramientas actualizadas${NC}"
echo ""

# ============================================
# PASO 4: Instalar Dependencias del Proyecto
# ============================================
echo -e "${YELLOW}[4/8] Instalando dependencias del proyecto...${NC}"

if [ -f "requirements.txt" ]; then
    echo -e "${BLUE}⏳ Instalando desde requirements.txt...${NC}"
    pip install -r requirements.txt -q
    echo -e "${GREEN}✓ Dependencias instaladas${NC}"
else
    echo -e "${RED}✗ requirements.txt no encontrado en $WORK_DIR${NC}"
    exit 1
fi
echo ""

# ============================================
# PASO 5: Crear .env desde template
# ============================================
echo -e "${YELLOW}[5/8] Configurando variables de entorno...${NC}"

if [ -f ".env" ]; then
    echo -e "${YELLOW}⚠ .env ya existe, saltando...${NC}"
else
    if [ -f ".env.example" ]; then
        cp .env.example .env
        echo -e "${GREEN}✓ .env creado desde .env.example${NC}"
        echo -e "${YELLOW}⚠ IMPORTANTE: Edita .env y añade tu HF_TOKEN${NC}"
    else
        echo -e "${YELLOW}⚠ .env.example no encontrado${NC}"
    fi
fi
echo ""

# ============================================
# PASO 6: Verificar Instalación
# ============================================
echo -e "${YELLOW}[6/8] Verificando instalación...${NC}"
python << 'PYEOF'
import sys
print(f"✓ Python: {sys.version.split()[0]}")

try:
    import transformers
    print(f"✓ Transformers: {transformers.__version__}")
except ImportError:
    print("✗ Transformers no instalado")

try:
    import torch
    print(f"✓ PyTorch: {torch.__version__}")
    import torch.cuda
    if torch.cuda.is_available():
        print(f"✓ CUDA disponible: {torch.cuda.get_device_name(0)}")
    else:
        print("✓ CUDA no disponible (usará CPU)")
except ImportError:
    print("✗ PyTorch no instalado")

try:
    import datasets
    print(f"✓ Datasets: {datasets.__version__}")
except ImportError:
    print("✗ Datasets no instalado")

try:
    from huggingface_hub import HfApi
    print(f"✓ Hugging Face Hub API disponible")
except ImportError:
    print("✗ Hugging Face Hub no instalado")
PYEOF
echo -e "${GREEN}✓ Verificación completada${NC}"
echo ""

# ============================================
# PASO 7: Inicializar Git (OPCIONAL)
# ============================================
if [ "$HAS_GIT" = true ]; then
    echo -e "${YELLOW}[7/8] Configurando Git y GitHub...${NC}"
    
    # Verificar si ya es un repo git
    if [ -d ".git" ]; then
        echo -e "${YELLOW}⚠ Ya es un repositorio git${NC}"
    else
        echo -e "${BLUE}Inicializando repositorio Git...${NC}"
        
        # Pedir datos del usuario
        read -p "Nombre completo (para Git commit): " GIT_NAME
        read -p "Email (para Git commit): " GIT_EMAIL
        
        # Inicializar git
        git init
        git config user.name "$GIT_NAME"
        git config user.email "$GIT_EMAIL"
        
        echo -e "${GREEN}✓ Repositorio Git inicializado${NC}"
        
        # Primer commit
        echo -e "${BLUE}Creando primer commit...${NC}"
        git add .
        git commit -m "Initial commit: Flujo A+B en 4 Horas" -q
        echo -e "${GREEN}✓ Primer commit creado${NC}"
    fi
    echo ""
    
    # Crear repositorio en GitHub
    read -p "¿Deseas crear un repositorio en GitHub? (s/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Ss]$ ]]; then
        echo -e "${BLUE}Para crear el repositorio en GitHub:${NC}"
        echo ""
        echo "1. Abre https://github.com/new"
        echo "2. Nombre del repo: $REPO_NAME"
        echo "3. Descripción: 'Flujo A+B en 4 Horas - Hugging Face Workflow'"
        echo "4. Público o privado (tu preferencia)"
        echo "5. NO inicialices con README (ya tenemos archivos)"
        echo ""
        echo -e "${YELLOW}Una vez creado el repositorio, ejecuta:${NC}"
        echo "   git remote add origin https://github.com/TU_USUARIO/$REPO_NAME.git"
        echo "   git branch -M main"
        echo "   git push -u origin main"
        echo ""
        echo -e "${YELLOW}⚠ Reemplaza TU_USUARIO con tu nombre de usuario en GitHub${NC}"
        echo ""
    fi
    echo ""
else
    echo -e "${YELLOW}[7/8] Git no disponible (saltando)${NC}"
    echo ""
fi

# ============================================
# PASO 8: Crear Dataset en Hugging Face Hub (OPCIONAL)
# ============================================
echo -e "${YELLOW}[8/8] Configurar Hugging Face Hub (OPCIONAL)${NC}"

# Verificar que HF_TOKEN está en .env
if grep -q "HF_TOKEN=" .env 2>/dev/null; then
    read -p "¿Deseas crear un dataset en Hugging Face Hub? (s/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Ss]$ ]]; then
        echo -e "${BLUE}Para crear el dataset en Hugging Face Hub:${NC}"
        echo ""
        echo "1. Abre https://huggingface.co/new-dataset"
        echo "2. Nombre: $PROJECT_NAME"
        echo "3. Descripción: 'Fine-tuned DistilBERT para análisis de sentimientos'"
        echo "4. Licencia: Elige la que prefieras (ej: MIT)"
        echo "5. Público o privado (tu preferencia)"
        echo ""
        echo -e "${YELLOW}El dataset se usará para guardar el modelo entrenado.${NC}"
        echo "Para publicar el modelo desde el script train_and_push.py:"
        echo "   - Edita configs/B_train.yaml"
        echo "   - Cambia: hf_repo_id: TU_USUARIO_HF/$PROJECT_NAME"
        echo ""
    fi
else
    echo -e "${YELLOW}⚠ HF_TOKEN no configurado en .env${NC}"
    echo "Para crear recursos en Hugging Face Hub, primero:"
    echo "  1. Edita .env y añade: HF_TOKEN=hf_xxxxxxxxx"
    echo "  2. Luego sigue los pasos anteriores"
fi
echo ""

# ============================================
# INFORMACIÓN FINAL
# ============================================
echo "=========================================="
echo -e "${GREEN}✅ INSTALACIÓN COMPLETADA${NC}"
echo "=========================================="
echo ""
echo -e "${BLUE}📋 Estado del entorno:${NC}"
echo "   Nombre: $ENV_NAME"
echo "   Ubicación: $WORK_DIR/$ENV_NAME"
echo "   Estado: ACTIVADO"
if [ "$HAS_GPU" = true ]; then
    echo "   GPU: DISPONIBLE ✓"
else
    echo "   GPU: No disponible (usará CPU)"
fi
echo ""
echo -e "${BLUE}📝 Próximos pasos:${NC}"
echo ""
echo "1️⃣  Edita .env y añade tu HF_TOKEN:"
echo "   nano .env"
echo "   # Descomenta: HF_TOKEN=hf_xxxxxxxxxxxx"
echo ""
echo "2️⃣  Lee la guía paso a paso:"
echo "   cat README_PASO_A_PASO.md"
echo ""
echo "3️⃣  O accede rápidamente al SETUP:"
echo "   cat SETUP.md"
echo ""
echo "4️⃣  Ejecuta Flujo A (Baseline - 1 min):"
echo "   python src/A_inferencia/predict_baseline.py"
echo ""
echo "5️⃣  Ejecuta Flujo B (Fine-tuning - 30 min GPU / 3h CPU):"
echo "   python src/B_finetuning/train_and_push.py"
echo ""
echo -e "${BLUE}🧪 Verificación rápida:${NC}"
echo "   python -c \"import transformers; print(f'✓ Transformers {transformers.__version__}')\""
echo ""
if [ "$HAS_GIT" = true ]; then
    echo -e "${BLUE}📦 Git Status:${NC}"
    echo "   git log --oneline  # Ver commits"
    echo "   git status         # Ver cambios"
    echo ""
fi
echo -e "${YELLOW}⚠ El entorno está ACTIVADO.${NC}"
echo "   Para desactivarlo: deactivate"
echo ""
echo "=========================================="
echo -e "${GREEN}🎉 ¡Listo para usar el proyecto!${NC}"
echo "=========================================="
echo ""
