# 🏗️ ARQUITECTURA DEL PROYECTO - ANÁLISIS DE COLAS M/M/1/K/Inf

## 📁 ESTRUCTURA DE CARPETAS

```
AnalisisColaM-M-1-K-Inf/
├── 📁 src/                    # Código fuente principal
│   ├── 📄 analisis_colas.py   # ⭐ ARCHIVO PRINCIPAL - TODO EN UNO
│   ├── 📄 formulas.py         # Solo fórmulas teóricas
│   └── 📄 simulacion.py       # Solo simulación
├── 📁 docs/                   # Documentación
│   ├── 📄 INSTRUCCIONES.md    # Guía de uso
│   └── 📄 TEORIA.md          # Explicación teórica
├── 📁 examples/               # Ejemplos de uso
│   ├── 📄 ejemplo_basico.py   # Ejemplo simple
│   └── 📄 ejemplo_avanzado.py # Ejemplo con múltiples configuraciones
├── 📄 README.md              # Descripción general
└── 📄 requirements.txt       # Dependencias (opcional)
```

## 🎯 ARCHIVOS PRINCIPALES

### 1. `src/analisis_colas.py` - ⭐ **ARCHIVO PRINCIPAL**
**Este es el único archivo que necesitas para la tarea**
- ✅ Fórmulas teóricas completas
- ✅ Simulación computacional
- ✅ Comparación de resultados
- ✅ Configuración fácil
- ✅ Sin dependencias externas

### 2. `docs/INSTRUCCIONES.md` - 📖 **GUÍA DE USO**
- Cómo cambiar parámetros
- Ejemplos de configuración
- Interpretación de resultados

### 3. `examples/` - 💡 **EJEMPLOS**
- Casos de uso comunes
- Diferentes configuraciones
- Comparaciones

## 🚀 USO RÁPIDO

### Para tu tarea (recomendado):
```bash
cd src/
python analisis_colas.py
```

### Para ejemplos:
```bash
cd examples/
python ejemplo_basico.py
```

## 🔧 CONFIGURACIÓN

En `src/analisis_colas.py`, cambia estas líneas:

```python
# ========================================
# CONFIGURACIÓN DE PARÁMETROS
# ========================================
LAMBDA = 0.9    # λ (tasa de llegada)
MU = 1.4        # μ (tasa de servicio)
K = 5           # K (capacidad del sistema)
MAX_TIME = 50000  # Tiempo de simulación
NUM_RUNS = 5    # Número de ejecuciones
```

## 📊 FLUJO DE TRABAJO

1. **Configurar parámetros** → Editar `src/analisis_colas.py`
2. **Ejecutar análisis** → `python src/analisis_colas.py`
3. **Ver resultados** → Comparación teórico vs simulado
4. **Interpretar** → Usar `docs/INSTRUCCIONES.md`

## 🎓 ARCHIVOS OPCIONALES

- `src/formulas.py` - Solo si quieres usar solo las fórmulas
- `src/simulacion.py` - Solo si quieres usar solo la simulación
- `examples/` - Para casos de uso específicos
- `docs/TEORIA.md` - Para entender la teoría detrás

## ⚡ VENTAJAS DE ESTA ARQUITECTURA

- ✅ **Simple**: Un solo archivo principal
- ✅ **Organizado**: Código separado por función
- ✅ **Documentado**: Guías claras
- ✅ **Extensible**: Fácil agregar nuevos ejemplos
- ✅ **Limpio**: Sin archivos innecesarios
