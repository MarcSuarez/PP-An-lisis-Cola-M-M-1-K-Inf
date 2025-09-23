# Análisis de Sistema de Colas M/M/1/K/Inf

Este proyecto implementa el análisis de un sistema de colas M/M/1/K/Inf usando tanto fórmulas teóricas como simulación computacional con Mesa.

## Descripción del Sistema

- **M/M/1/K/Inf**: Sistema de colas con:
  - **M**: Llegadas siguiendo proceso de Poisson
  - **M**: Tiempos de servicio exponenciales
  - **1**: Un servidor
  - **K**: Capacidad limitada del sistema
  - **Inf**: Población infinita

## Archivos del Proyecto

- `theoretical_formulas.py`: Implementa las fórmulas teóricas para calcular NS, TS, Nw, Tw
- `queue_simulation.py`: Simulación del sistema usando Mesa
- `main.py`: Programa principal que ejecuta el análisis completo
- `requirements.txt`: Dependencias de Python necesarias

## Instalación

1. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Uso

### Ejecución básica (parámetros por defecto)
```bash
python main.py
```

### Ejecución con parámetros personalizados
```bash
python main.py --lambda 0.8 --mu 1.2 --K 4 --time 100000 --runs 10
```

### Solo resultados teóricos
```bash
python main.py --theoretical-only
```

### Solo simulación
```bash
python main.py --simulation-only
```

## Parámetros

- `--lambda`: Tasa de llegada λ (default: 0.9)
- `--mu`: Tasa de servicio μ (default: 1.4)
- `--K`: Capacidad del sistema K (default: 5)
- `--time`: Tiempo máximo de simulación (default: 50000)
- `--runs`: Número de ejecuciones para promediar (default: 5)

## Métricas Calculadas

- **NS**: Número promedio de usuarios en el sistema
- **TS**: Tiempo promedio en el sistema
- **Nw**: Número promedio de usuarios en cola
- **Tw**: Tiempo promedio en cola

## Ejemplo de Salida

```
ANÁLISIS DE SISTEMA DE COLAS M/M/1/K/Inf
==================================================
Parámetros de entrada:
  λ (tasa de llegada): 0.9
  μ (tasa de servicio): 1.4
  K (capacidad): 5
  ρ (utilización): 0.6429

============================================================
RESULTADOS TEÓRICOS - SISTEMA M/M/1/K/Inf
============================================================
Parámetros:
  λ (tasa de llegada): 0.9000
  μ (tasa de servicio): 1.4000
  K (capacidad): 5
  ρ (utilización): 0.6429

Resultados:
  NS (usuarios en sistema): 1.2345
  TS (tiempo en sistema): 1.6789
  Nw (usuarios en cola): 0.5916
  Tw (tiempo en cola): 0.8045

================================================================================
RESULTADOS COMPARATIVOS
================================================================================
Métrica          Teórico     Simulado    Diferencia   Error %   
--------------------------------------------------------------------------------
NS              1.2345      1.2456      0.0111       0.90      
TS              1.6789      1.6923      0.0134       0.80      
Nw              0.5916      0.5987      0.0071       1.20      
Tw              0.8045      0.8123      0.0078       0.97      
```

## Comparación con NetLogo

Este modelo Python replica la funcionalidad del modelo NetLogo original, pero se enfoca específicamente en el sistema M/M/1/K/Inf. Las principales diferencias:

1. **Especialización**: Solo maneja 1 servidor con capacidad limitada
2. **Fórmulas teóricas**: Implementa las fórmulas específicas para M/M/1/K
3. **Análisis estadístico**: Incluye análisis de convergencia y múltiples ejecuciones

## Referencias

- Mesa Documentation: https://mesa.readthedocs.io/
- Teoría de Colas: Gross, D., & Harris, C. M. (1998). Fundamentals of queueing theory
