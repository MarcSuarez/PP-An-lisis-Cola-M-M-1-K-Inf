"""
EJEMPLO BÁSICO - Análisis de Colas M/M/1/K/Inf
==============================================

Este ejemplo muestra cómo usar el análisis de colas con una configuración básica.
"""

import sys
import os

# Agregar el directorio src al path para importar el módulo
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from analisis_colas import run_complete_analysis

def main():
    """Ejemplo básico de análisis de colas"""
    
    print("=" * 60)
    print("EJEMPLO BÁSICO - ANÁLISIS DE COLAS M/M/1/K/Inf")
    print("=" * 60)
    
    # Configuración básica
    lambda_rate = 0.8    # λ = 0.8 clientes/minuto
    mu_rate = 1.2        # μ = 1.2 clientes/minuto
    K = 4                # K = 4 (capacidad total)
    max_time = 30000     # 30,000 unidades de tiempo
    num_runs = 3         # 3 ejecuciones para promediar
    
    print(f"Configuración:")
    print(f"  λ (tasa de llegada): {lambda_rate}")
    print(f"  μ (tasa de servicio): {mu_rate}")
    print(f"  K (capacidad): {K}")
    print(f"  Tiempo de simulación: {max_time}")
    print(f"  Número de ejecuciones: {num_runs}")
    print()
    
    # Ejecutar análisis completo
    theoretical, simulated, results = run_complete_analysis(
        lambda_rate, mu_rate, K, max_time, num_runs
    )
    
    # Mostrar resumen
    print("\n" + "=" * 60)
    print("RESUMEN DEL EJEMPLO")
    print("=" * 60)
    print("✅ Análisis completado exitosamente")
    print("✅ Resultados teóricos calculados")
    print("✅ Simulación ejecutada")
    print("✅ Comparación realizada")
    print("\nLos resultados muestran la concordancia entre")
    print("los valores teóricos y los simulados.")

if __name__ == "__main__":
    main()
