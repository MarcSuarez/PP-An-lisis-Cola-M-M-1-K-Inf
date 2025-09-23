"""
Fórmulas teóricas para el sistema de colas M/M/1/K/Inf
Sistema con 1 servidor, capacidad K, población infinita
"""

import math

def mm1k_theoretical_values(lambda_rate, mu_rate, K):
    """
    Calcula los valores teóricos para un sistema M/M/1/K/Inf
    
    Parámetros:
    - lambda_rate: tasa de llegada (λ)
    - mu_rate: tasa de servicio (μ)
    - K: capacidad del sistema (incluyendo el servidor)
    
    Retorna:
    - NS: número promedio de usuarios en el sistema
    - TS: tiempo promedio en el sistema
    - Nw: número promedio de usuarios en cola
    - Tw: tiempo promedio en cola
    """
    
    # Factor de utilización
    rho = lambda_rate / mu_rate
    
    # Probabilidades de estado
    if rho == 1:
        # Caso especial cuando rho = 1
        p0 = 1 / (K + 1)  # Probabilidad de sistema vacío
        pn = 1 / (K + 1)  # Probabilidad de n usuarios (uniforme)
    else:
        # Caso general
        p0 = (1 - rho) / (1 - rho**(K + 1))  # Probabilidad de sistema vacío
        pn = lambda n: p0 * (rho**n)  # Probabilidad de n usuarios
    
    # Número promedio de usuarios en el sistema (NS)
    if rho == 1:
        NS = K / 2
    else:
        NS = rho * (1 - (K + 1) * rho**K + K * rho**(K + 1)) / ((1 - rho) * (1 - rho**(K + 1)))
    
    # Tasa efectiva de llegada (considerando pérdidas por capacidad)
    lambda_eff = lambda_rate * (1 - pn(K))
    
    # Tiempo promedio en el sistema (TS) - Fórmula de Little
    TS = NS / lambda_eff
    
    # Número promedio de usuarios en cola (Nw)
    # NS = Nw + (probabilidad de que el servidor esté ocupado)
    server_busy_prob = 1 - p0
    Nw = NS - server_busy_prob
    
    # Tiempo promedio en cola (Tw)
    Tw = Nw / lambda_eff
    
    return {
        'NS': NS,
        'TS': TS,
        'Nw': Nw,
        'Tw': Tw,
        'rho': rho,
        'p0': p0,
        'lambda_eff': lambda_eff,
        'server_busy_prob': server_busy_prob
    }

def print_theoretical_results(lambda_rate, mu_rate, K):
    """Imprime los resultados teóricos de forma organizada"""
    results = mm1k_theoretical_values(lambda_rate, mu_rate, K)
    
    print("=" * 60)
    print("RESULTADOS TEÓRICOS - SISTEMA M/M/1/K/Inf")
    print("=" * 60)
    print(f"Parámetros:")
    print(f"  λ (tasa de llegada): {lambda_rate:.4f}")
    print(f"  μ (tasa de servicio): {mu_rate:.4f}")
    print(f"  K (capacidad): {K}")
    print(f"  ρ (utilización): {results['rho']:.4f}")
    print()
    print(f"Resultados:")
    print(f"  NS (usuarios en sistema): {results['NS']:.4f}")
    print(f"  TS (tiempo en sistema): {results['TS']:.4f}")
    print(f"  Nw (usuarios en cola): {results['Nw']:.4f}")
    print(f"  Tw (tiempo en cola): {results['Tw']:.4f}")
    print()
    print(f"Información adicional:")
    print(f"  Probabilidad sistema vacío (p0): {results['p0']:.4f}")
    print(f"  Tasa efectiva de llegada: {results['lambda_eff']:.4f}")
    print(f"  Probabilidad servidor ocupado: {results['server_busy_prob']:.4f}")
    print("=" * 60)
    
    return results

if __name__ == "__main__":
    # ========================================
    # CONFIGURACIÓN DE PARÁMETROS
    # ========================================
    # Cambia estos valores según tus necesidades:
    # λ (lambda) = tasa de llegada (clientes por unidad de tiempo)
    # μ (mu) = tasa de servicio (clientes atendidos por unidad de tiempo)
    # K = capacidad del sistema (incluyendo el servidor)
    
    lambda_rate = 0.9  # CAMBIAR: Tasa de llegada λ
    mu_rate = 1.4      # CAMBIAR: Tasa de servicio μ  
    K = 5              # CAMBIAR: Capacidad del sistema K
    
    # Ejemplo de expresiones algebraicas:
    # lambda_rate = 100  # λ = 100 clientes/hora
    # mu_rate = 150      # μ = 150 clientes/hora
    # K = 10             # K = 10 (capacidad total)
    
    print_theoretical_results(lambda_rate, mu_rate, K)
