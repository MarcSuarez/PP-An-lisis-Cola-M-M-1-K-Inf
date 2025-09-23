# INSTRUCCIONES DE USO - ANÁLISIS DE COLAS M/M/1/K/Inf

## 🎯 OBJETIVO
Comprobar los resultados teóricos de un sistema de colas M/M/1/K/Inf usando simulación computacional.

## 📁 ARCHIVOS PRINCIPALES

### `analisis_colas.py` - ARCHIVO PRINCIPAL ⭐
**Este es el archivo que debes usar.** Contiene todo lo necesario:
- Fórmulas teóricas
- Simulación computacional
- Comparación de resultados

### Otros archivos (opcionales):
- `theoretical_formulas.py` - Solo fórmulas teóricas
- `simple_simulation.py` - Solo simulación simple
- `queue_simulation.py` - Simulación con Mesa (requiere instalación)

## 🚀 USO RÁPIDO

### 1. Cambiar los parámetros
Abre `analisis_colas.py` y modifica estas líneas:

```python
# ========================================
# CONFIGURACIÓN DE PARÁMETROS
# ========================================
# CAMBIA ESTOS VALORES SEGÚN TUS NECESIDADES:

LAMBDA = 0.9    # λ (lambda) = tasa de llegada
MU = 1.4        # μ (mu) = tasa de servicio  
K = 5           # K = capacidad del sistema
MAX_TIME = 50000  # Tiempo máximo de simulación
NUM_RUNS = 5    # Número de ejecuciones para promediar
```

### 2. Ejecutar el análisis
```bash
python analisis_colas.py
```

## 📊 RESULTADOS QUE OBTIENES

El programa calcula y compara:

- **NS**: Número promedio de usuarios en el sistema
- **TS**: Tiempo promedio en el sistema  
- **Nw**: Número promedio de usuarios en cola
- **Tw**: Tiempo promedio en cola

### Ejemplo de salida:
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

## 🔧 EJEMPLOS DE CONFIGURACIÓN

### Ejemplo 1: Sistema con alta utilización
```python
LAMBDA = 1.2    # λ = 1.2 clientes/minuto
MU = 1.5        # μ = 1.5 clientes/minuto
K = 8           # K = 8 (capacidad total)
```

### Ejemplo 2: Sistema con baja utilización
```python
LAMBDA = 0.5    # λ = 0.5 clientes/minuto
MU = 2.0        # μ = 2.0 clientes/minuto
K = 3           # K = 3 (capacidad total)
```

### Ejemplo 3: Sistema con capacidad grande
```python
LAMBDA = 100    # λ = 100 clientes/hora
MU = 120        # μ = 120 clientes/hora
K = 50          # K = 50 (capacidad total)
```

## 📈 INTERPRETACIÓN DE RESULTADOS

### Error porcentual aceptable:
- **< 5%**: Excelente concordancia
- **5-10%**: Buena concordancia
- **10-20%**: Concordancia aceptable
- **> 20%**: Revisar parámetros o aumentar tiempo de simulación

### Factores que afectan la precisión:
1. **Tiempo de simulación**: Mayor tiempo = mayor precisión
2. **Número de ejecuciones**: Más ejecuciones = mejor promedio
3. **Utilización (ρ)**: Valores extremos pueden requerir más tiempo

## ⚠️ NOTAS IMPORTANTES

1. **No requiere instalación**: El archivo `analisis_colas.py` solo usa librerías estándar de Python
2. **Tiempo de ejecución**: Simulaciones largas pueden tomar varios minutos
3. **Valores de entrada**: Asegúrate de que λ, μ y K sean positivos
4. **Estabilidad**: Para ρ ≥ 1, el sistema puede ser inestable (pero K limita la capacidad)

## 🎓 CONCEPTOS TEÓRICOS

### Sistema M/M/1/K/Inf:
- **M**: Llegadas siguiendo proceso de Poisson
- **M**: Tiempos de servicio exponenciales
- **1**: Un servidor
- **K**: Capacidad limitada del sistema
- **Inf**: Población infinita

### Fórmulas utilizadas:
- **Utilización**: ρ = λ/μ
- **Probabilidad sistema vacío**: p₀ = (1-ρ)/(1-ρ^(K+1))
- **Número en sistema**: NS = ρ(1-(K+1)ρ^K + Kρ^(K+1))/((1-ρ)(1-ρ^(K+1)))
- **Fórmula de Little**: NS = λ_eff × TS

## 🔍 COMPARACIÓN CON NETLOGO

Este modelo Python replica la funcionalidad del modelo NetLogo original, pero:
- Se enfoca específicamente en M/M/1/K/Inf
- Incluye fórmulas teóricas específicas
- Proporciona análisis estadístico detallado
- Es más fácil de modificar y usar

## 📞 SOPORTE

Si tienes problemas:
1. Verifica que los parámetros sean positivos
2. Aumenta el tiempo de simulación si los errores son altos
3. Revisa que Python esté instalado correctamente
