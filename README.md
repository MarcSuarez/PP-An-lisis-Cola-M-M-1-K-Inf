# 📊 Análisis de Sistema de Colas M/M/1/K/Inf

> **Análisis completo de un sistema de colas con 1 servidor, capacidad limitada K y población infinita**

## 🎯 Objetivo

Comprobar los resultados teóricos de un sistema de colas M/M/1/K/Inf usando simulación computacional para encontrar:
- **NS**: Número promedio de usuarios en el sistema
- **TS**: Tiempo promedio en el sistema
- **Nw**: Número promedio de usuarios en cola
- **Tw**: Tiempo promedio en cola

## 🚀 Uso Rápido

### 1. Ejecutar análisis básico
```bash
cd src/
python analisis_colas.py
```

### 2. Ver ejemplos
```bash
cd examples/
python ejemplo_basico.py
```

## 📁 Estructura del Proyecto

```
📁 src/                    # Código fuente
│   └── 📄 analisis_colas.py   # ⭐ ARCHIVO PRINCIPAL
📁 examples/               # Ejemplos de uso
│   ├── 📄 ejemplo_basico.py
│   └── 📄 ejemplo_avanzado.py
📁 docs/                   # Documentación
│   ├── 📄 INSTRUCCIONES.md
│   └── 📄 ARQUITECTURA.md
```

## ⚙️ Configuración

Edita `src/analisis_colas.py`:

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

## 📊 Ejemplo de Resultados

```
COMPARACIÓN TEÓRICA vs SIMULADA
================================================================================
Métrica         Teórico      Simulado     Diferencia   Error %   
--------------------------------------------------------------------------------
NS              1.3444       1.3504       0.0061       0.45      
TS              1.5595       1.5601       0.0005       0.03      
Nw              0.7286       0.7334       0.0048       0.66      
Tw              0.8452       0.8473       0.0021       0.25      
```

## 🎓 Sistema M/M/1/K/Inf

- **M**: Llegadas siguiendo proceso de Poisson
- **M**: Tiempos de servicio exponenciales
- **1**: Un servidor
- **K**: Capacidad limitada del sistema
- **Inf**: Población infinita

## ✅ Características

- ✅ **Sin dependencias externas** (solo Python estándar)
- ✅ **Fácil de configurar** con comentarios claros
- ✅ **Resultados precisos** (errores < 1% típicamente)
- ✅ **Comparación directa** teórico vs simulado
- ✅ **Basado en modelo NetLogo** existente

## 📖 Documentación

- [📋 Instrucciones detalladas](docs/INSTRUCCIONES.md)
- [🏗️ Arquitectura del proyecto](docs/ARQUITECTURA.md)

## 🔧 Requisitos

- Python 3.6+
- No se requieren librerías externas

## 📝 Uso para Tarea Académica

1. **Configura los parámetros** en `src/analisis_colas.py`
2. **Ejecuta el análisis**: `python src/analisis_colas.py`
3. **Interpreta los resultados** usando la documentación
4. **Compara** con los valores del modelo NetLogo original

---

**Desarrollado para análisis académico de sistemas de colas M/M/1/K/Inf**
