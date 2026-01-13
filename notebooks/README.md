# 📓 Notebooks - Estructura de Tareas Básicas

Dos cuadernos para el flujo completo A→B→A del proyecto.

## 🔄 Flujo de Ejecución

```
1. Flujo_A_Inferencia.ipynb (Paso 2: Modelo Base)
   ↓
2. Flujo_B_FineTuning.ipynb (Entrenamiento Completo)
   ↓
3. Flujo_A_Inferencia.ipynb (Paso 3: Modelo Custom)
```

---

## 📘 Flujo_A_Inferencia.ipynb

**Propósito**: Probar predicciones con modelo base y modelo fine-tuneado.

### Tareas Básicas

**Paso 1: Setup**
- Importar librerías
- Cargar variables de entorno (.env)
- Configurar rutas del proyecto

**Paso 2: Modelo Base (FLUJO A1)**
- Cargar configuración A_baseline.yaml
- Crear pipeline para sentiment-analysis
- Realizar predicción con texto de prueba
- Mostrar resultado

**Paso 3: Modelo Custom (FLUJO A2)**
- Cargar configuración A_finetuned.yaml
- Crear pipeline para sentiment-analysis
- Realizar predicción con MISMO texto
- Mostrar resultado

**Paso 4: Comparación**
- Tabla comparativa (base vs fine-tuned)
- Análisis de diferencias
- Tasa de concordancia

**Paso 5: Área Libre**
- Probar textos personalizados
- Experimentar con diferentes ejemplos

---

## 🚀 Flujo_B_FineTuning.ipynb

**Propósito**: Entrenamiento y publicación del modelo en Hub.

### Tareas Básicas

**Paso 1: Setup**
- Importar librerías
- Cargar configuración
- Verificar GPU

**Paso 2: Autenticación**
- Verificar HF_TOKEN
- Login en Hugging Face Hub

**Paso 3: Datos**
- Cargar dataset SST2
- Crear subsets (reducidos para rapidez)
- Mostrar ejemplos

**Paso 4: Modelo**
- Cargar modelo y tokenizador
- Tokenizar dataset
- Preparar formato torch

**Paso 5: Entrenamiento**
- Configurar argumentos
- Crear Trainer
- **Entrenar** (⏱️ 30 min GPU / 3h CPU)

**Paso 6: Evaluación**
- Evaluar modelo
- Mostrar métricas finales

**Paso 7: Publicación**
- Push a Hugging Face Hub
- Mostrar URL del repositorio

---

## 📊 Tabla de Ejecución Recomendada

| Notebook | Duración | GPU | CPU | Orden |
|----------|----------|-----|-----|-------|
| Flujo_A_Inferencia (Paso 2) | 2 min | ✓ | ✓ | 1º |
| Flujo_B_FineTuning | 30 min | ✓ | 3h | 2º |
| Flujo_A_Inferencia (Paso 3) | 2 min | ✓ | ✓ | 3º |

---

## 🎯 Tareas por Celda (Mínimo)

### Flujo A
- [ ] **Celda 1**: Importaciones + Setup
- [ ] **Celda 2**: Load config baseline
- [ ] **Celda 3**: Create pipeline baseline
- [ ] **Celda 4**: Predict baseline
- [ ] **Celda 5**: Load config finetuned
- [ ] **Celda 6**: Create pipeline finetuned
- [ ] **Celda 7**: Predict finetuned
- [ ] **Celda 8**: Compare results

### Flujo B
- [ ] **Celda 1**: Importaciones + Setup
- [ ] **Celda 2**: Load config
- [ ] **Celda 3**: Login HF
- [ ] **Celda 4**: Load dataset
- [ ] **Celda 5**: Create subsets
- [ ] **Celda 6**: Load model + tokenizer
- [ ] **Celda 7**: Tokenize dataset
- [ ] **Celda 8**: Configure training
- [ ] **Celda 9**: Train model (⏱️)
- [ ] **Celda 10**: Evaluate
- [ ] **Celda 11**: Push to Hub

---

## 💡 Notas Importantes

1. **Flujo A es rápido**: 2-3 minutos por paso
2. **Flujo B toma tiempo**: 30 min (GPU) o 3 horas (CPU)
3. **Orden es crítico**: B debe completarse antes de probar Flujo A paso 3
4. **Token HF**: Necesario para Flujo B
5. **Subsets reducidos**: El notebook usa 5000 train + 1000 eval para rapidez

---

## 📝 Checklist de Ejecución

```bash
# Antes de empezar
[ ] HF_TOKEN configurado en .env
[ ] Conexión a internet
[ ] GPU disponible (recomendado para Flujo B)

# Flujo A - Paso 2
[ ] Setup completado
[ ] Config baseline cargada
[ ] Pipeline creado
[ ] Predicción realizada

# Flujo B
[ ] Autenticación OK
[ ] Dataset descargado
[ ] Modelo entrenado
[ ] Publicado en Hub

# Flujo A - Paso 3
[ ] Config finetuned cargada
[ ] Pipeline creado
[ ] Predicción realizada
[ ] Comparación hecha
```

---

## 🔗 Enlaces Útiles

- [Hugging Face Hub](https://huggingface.co)
- [Transformers Docs](https://huggingface.co/docs/transformers)
- [SST2 Dataset](https://huggingface.co/datasets/glue/viewer/sst2)
- [DistilBERT Model](https://huggingface.co/distilbert-base-uncased)

