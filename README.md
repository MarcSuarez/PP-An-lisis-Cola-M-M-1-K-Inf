# Análisis de Sistema de Colas M/M/1/K/Inf

## Descripción

Este proyecto implementa el análisis completo de un sistema de colas M/M/1/K/Inf (Markov/Markov/1 servidor/capacidad K/población infinita) para calcular las métricas principales:

- **NS**: Número promedio de usuarios en el sistema
- **TS**: Tiempo promedio en el sistema  
- **Nw**: Número promedio de usuarios en cola
- **Tw**: Tiempo promedio en cola

## Estructura del Proyecto

```
src/
├── analisis_colas.py    # Modelo matemático + simulación simple
└── mesa_mm1k.py         # Verificación con Mesa (headless)
archivos_netlogo/
└── Discrete_Event_Simulation__Queues_and_Servers.nlogo
```

## Requisitos

- Python 3.6+
- Mesa (solo para verificación con Mesa)

## Instalación

```bash
# Para verificación con Mesa (opcional)
pip install -U "mesa[rec]"
```

## Uso

### 1. Análisis Matemático + Simulación Simple

```bash
cd src/
python analisis_colas.py
```

Este comando ejecuta:
- Cálculo de fórmulas teóricas
- Simulación de eventos discretos
- Comparación teórico vs simulado

### 2. Verificación con Mesa

```bash
cd src/
python -c "from mesa_mm1k import run_mesa_mm1k; print(run_mesa_mm1k(0.9,1.4,5,50000,5)[0])"
```

## Configuración de Parámetros

Edita las variables en `src/analisis_colas.py`:

```python
LAMBDA = 0.9    # λ (tasa de llegada)
MU = 1.4        # μ (tasa de servicio)  
K = 5           # K (capacidad del sistema)
MAX_TIME = 50000  # Tiempo de simulación
NUM_RUNS = 5    # Número de ejecuciones
```

## Ejemplo de Salida

```
RESULTADOS TEÓRICOS - SISTEMA M/M/1/K/Inf
============================================================
Parámetros:
  λ (tasa de llegada): 0.9000
  μ (tasa de servicio): 1.4000
  K (capacidad): 5

Resultados:
  NS (usuarios en sistema): 1.3444
  TS (tiempo en sistema): 1.5595
  Nw (usuarios en cola): 0.7286
  Tw (tiempo en cola): 0.8452
============================================================

COMPARACIÓN TEÓRICA vs SIMULADA
================================================================================
Métrica         Teórico      Simulado     Diferencia   Error %   
--------------------------------------------------------------------------------
NS              1.3444       1.3504       0.0061       0.45      
TS              1.5595       1.5601       0.0005       0.03      
Nw              0.7286       0.7334       0.0048       0.66      
Tw              0.8452       0.8473       0.0021       0.25      
```

## Archivos

- **`analisis_colas.py`**: Contiene las fórmulas teóricas del sistema M/M/1/K/Inf y una simulación de eventos discretos para verificar los resultados.
- **`mesa_mm1k.py`**: Implementación alternativa usando Mesa para verificación adicional.
- **`archivos_netlogo/`**: Modelo NetLogo original de referencia.

## Referencias

- Mesa documentation: https://mesa.readthedocs.io/latest/
- NetLogo model: Discrete Event Simulation - Queues and Servers
