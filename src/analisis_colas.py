"""
ANÁLISIS COMPLETO DE SISTEMA DE COLAS M/M/1/K/Inf
==================================================

Este archivo contiene todo lo necesario para analizar un sistema de colas M/M/1/K/Inf:
- Fórmulas teóricas
- Simulación computacional
- Comparación de resultados

Autor: Análisis de Colas M/M/1/K/Inf
Basado en: Modelo NetLogo de simulación de eventos discretos
"""

import random
import math

# ========================================
# CONFIGURACIÓN DE PARÁMETROS
# ========================================
# CAMBIA ESTOS VALORES SEGÚN TUS NECESIDADES:

LAMBDA = 0.9    # λ (lambda) = tasa de llegada (clientes por unidad de tiempo)
MU = 1.4        # μ (mu) = tasa de servicio (clientes atendidos por unidad de tiempo)
K = 5           # K = capacidad del sistema (incluyendo el servidor)
MAX_TIME = 50000  # Tiempo máximo de simulación
NUM_RUNS = 5    # Número de ejecuciones para promediar

# Ejemplos de expresiones algebraicas:
# LAMBDA = 100   # λ = 100 clientes/hora
# MU = 150       # μ = 150 clientes/hora  
# K = 10         # K = 10 (capacidad total)

# ========================================
# FÓRMULAS TEÓRICAS
# ========================================

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
        'Tw': Tw
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
    print()
    print(f"Resultados:")
    print(f"  NS (usuarios en sistema): {results['NS']:.4f}")
    print(f"  TS (tiempo en sistema): {results['TS']:.4f}")
    print(f"  Nw (usuarios en cola): {results['Nw']:.4f}")
    print(f"  Tw (tiempo en cola): {results['Tw']:.4f}")
    print("=" * 60)
    
    return results

# ========================================
# SIMULACIÓN COMPUTACIONAL
# ========================================

class SimpleQueueSimulation:
    """Simulación simple de eventos discretos para M/M/1/K/Inf"""
    
    def __init__(self, lambda_rate, mu_rate, K):
        self.lambda_rate = lambda_rate
        self.mu_rate = mu_rate
        self.K = K
        
        # Estado del sistema
        self.current_time = 0.0
        self.queue = []
        self.server_busy = False
        self.server_customer = None
        
        # Estadísticas
        self.total_arrivals = 0
        self.total_departures = 0
        self.total_blocked = 0
        self.total_queue_time = 0.0
        self.total_system_time = 0.0
        
        # Eventos
        self.next_arrival_time = 0.0
        self.next_service_completion_time = float('inf')
        
    def exponential_random(self, rate):
        """Genera un número aleatorio exponencial con la tasa dada"""
        return -math.log(1.0 - random.random()) / rate
    
    def schedule_next_arrival(self):
        """Programa la próxima llegada"""
        interarrival_time = self.exponential_random(self.lambda_rate)
        self.next_arrival_time = self.current_time + interarrival_time
        
    def schedule_service_completion(self, customer):
        """Programa la finalización del servicio"""
        service_time = self.exponential_random(self.mu_rate)
        self.next_service_completion_time = self.current_time + service_time
        customer['service_start_time'] = self.current_time
        
    def process_arrival(self):
        """Procesa la llegada de un cliente"""
        self.total_arrivals += 1
        
        customer = {
            'id': self.total_arrivals,
            'arrival_time': self.current_time,
            'service_start_time': None,
            'departure_time': None
        }
        
        # Verificar si hay espacio en el sistema
        customers_in_system = len(self.queue) + (1 if self.server_busy else 0)
        
        if customers_in_system < self.K:
            # Hay espacio, agregar al sistema
            if not self.server_busy:
                # Servidor libre, comenzar servicio inmediatamente
                self.server_busy = True
                self.server_customer = customer
                self.schedule_service_completion(customer)
            else:
                # Servidor ocupado, agregar a la cola
                self.queue.append(customer)
        else:
            # Sistema lleno, cliente bloqueado
            self.total_blocked += 1
            
        # Programar próxima llegada
        self.schedule_next_arrival()
        
    def process_service_completion(self):
        """Procesa la finalización del servicio"""
        if self.server_busy and self.server_customer:
            customer = self.server_customer
            
            # Calcular tiempos
            customer['departure_time'] = self.current_time
            queue_time = customer['service_start_time'] - customer['arrival_time']
            system_time = customer['departure_time'] - customer['arrival_time']
            
            # Actualizar estadísticas
            self.total_queue_time += queue_time
            self.total_system_time += system_time
            self.total_departures += 1
            
            # Liberar servidor
            self.server_busy = False
            self.server_customer = None
            self.next_service_completion_time = float('inf')
            
            # Si hay clientes en cola, comenzar servicio del siguiente
            if self.queue:
                next_customer = self.queue.pop(0)
                self.server_busy = True
                self.server_customer = next_customer
                self.schedule_service_completion(next_customer)
                
    def run_simulation(self, max_time):
        """Ejecuta la simulación hasta el tiempo máximo"""
        # Programar primera llegada
        self.schedule_next_arrival()
        
        while self.current_time < max_time:
            # Determinar el próximo evento
            if self.next_arrival_time < self.next_service_completion_time:
                # Próximo evento: llegada
                self.current_time = self.next_arrival_time
                self.process_arrival()
            else:
                # Próximo evento: finalización de servicio
                self.current_time = self.next_service_completion_time
                self.process_service_completion()
                
    def get_statistics(self):
        """Calcula y retorna las estadísticas de la simulación"""
        if self.total_departures == 0:
            return {
                'NS': 0, 'TS': 0, 'Nw': 0, 'Tw': 0
            }
            
        # Tasa efectiva de llegada
        lambda_eff = self.total_departures / self.current_time
        
        # Tiempo promedio en el sistema
        TS = self.total_system_time / self.total_departures
        
        # Tiempo promedio en cola
        Tw = self.total_queue_time / self.total_departures
        
        # Número promedio en el sistema (usando fórmula de Little)
        NS = lambda_eff * TS
        
        # Número promedio en cola
        Nw = lambda_eff * Tw
        
        return {
            'NS': NS,
            'TS': TS,
            'Nw': Nw,
            'Tw': Tw
        }

# ========================================
# FUNCIÓN PRINCIPAL
# ========================================

def run_complete_analysis(lambda_rate, mu_rate, K, max_time, num_runs):
    """
    Ejecuta el análisis completo: teórico + simulación + comparación
    """
    print("ANÁLISIS COMPLETO DE SISTEMA DE COLAS M/M/1/K/Inf")
    print("=" * 60)
    print(f"Parámetros:")
    print(f"  λ (tasa de llegada): {lambda_rate}")
    print(f"  μ (tasa de servicio): {mu_rate}")
    print(f"  K (capacidad): {K}")
    print(f"  Tiempo de simulación: {max_time}")
    print(f"  Número de ejecuciones: {num_runs}")
    print()
    
    # 1. Calcular valores teóricos
    print_theoretical_results(lambda_rate, mu_rate, K)
    theoretical = mm1k_theoretical_values(lambda_rate, mu_rate, K)
    
    print("\n" + "=" * 80)
    print("SIMULACIÓN COMPUTACIONAL")
    print("=" * 80)
    
    # 2. Ejecutar simulaciones
    results = []
    for run in range(num_runs):
        print(f"Ejecutando simulación {run + 1}/{num_runs}...")
        sim = SimpleQueueSimulation(lambda_rate, mu_rate, K)
        sim.run_simulation(max_time)
        stats = sim.get_statistics()
        results.append(stats)
    
    # 3. Calcular promedios
    avg_results = {}
    for key in ['NS', 'TS', 'Nw', 'Tw']:
        avg_results[key] = sum(r[key] for r in results) / len(results)
    
    # 4. Mostrar comparación
    print("\n" + "=" * 80)
    print("COMPARACIÓN TEÓRICA vs SIMULADA")
    print("=" * 80)
    
    print(f"{'Métrica':<15} {'Teórico':<12} {'Simulado':<12} {'Diferencia':<12} {'Error %':<10}")
    print("-" * 80)
    
    metrics = ['NS', 'TS', 'Nw', 'Tw']
    for metric in metrics:
        theoretical_val = theoretical[metric]
        simulated_val = avg_results[metric]
        difference = simulated_val - theoretical_val
        error_pct = abs(difference / theoretical_val * 100) if theoretical_val != 0 else 0
        
        print(f"{metric:<15} {theoretical_val:<12.4f} {simulated_val:<12.4f} {difference:<12.4f} {error_pct:<10.2f}")
    
    print("\n" + "=" * 80)
    print("ANÁLISIS COMPLETADO")
    print("=" * 80)
    
    return theoretical, avg_results, results

# ========================================
# EJECUCIÓN PRINCIPAL
# ========================================

if __name__ == "__main__":
    # Ejecutar análisis completo con los parámetros configurados
    run_complete_analysis(LAMBDA, MU, K, MAX_TIME, NUM_RUNS)
