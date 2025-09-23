"""
Simulación simple de sistema de colas M/M/1/K/Inf sin dependencias externas
Solo cálculos, sin visualización
"""

import random
import math
from theoretical_formulas import mm1k_theoretical_values

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
                'NS': 0, 'TS': 0, 'Nw': 0, 'Tw': 0,
                'lambda_eff': 0, 'blocking_prob': 0
            }
            
        # Tasa efectiva de llegada
        lambda_eff = self.total_departures / self.current_time
        
        # Probabilidad de bloqueo
        blocking_prob = self.total_blocked / self.total_arrivals if self.total_arrivals > 0 else 0
        
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
            'Tw': Tw,
            'lambda_eff': lambda_eff,
            'blocking_prob': blocking_prob,
            'total_arrivals': self.total_arrivals,
            'total_departures': self.total_departures,
            'total_blocked': self.total_blocked,
            'simulation_time': self.current_time
        }

def run_simple_simulation_and_compare(lambda_rate, mu_rate, K, max_time=50000, num_runs=5):
    """
    Ejecuta múltiples simulaciones simples y compara con los valores teóricos
    """
    print("=" * 80)
    print("SIMULACIÓN SIMPLE M/M/1/K/Inf - COMPARACIÓN TEÓRICA vs SIMULADA")
    print("=" * 80)
    
    # Calcular valores teóricos
    theoretical = mm1k_theoretical_values(lambda_rate, mu_rate, K)
    
    print(f"Parámetros:")
    print(f"  λ (tasa de llegada): {lambda_rate:.4f}")
    print(f"  μ (tasa de servicio): {mu_rate:.4f}")
    print(f"  K (capacidad): {K}")
    print(f"  Tiempo de simulación: {max_time}")
    print(f"  Número de ejecuciones: {num_runs}")
    print()
    
    # Ejecutar simulaciones
    results = []
    for run in range(num_runs):
        print(f"Ejecutando simulación {run + 1}/{num_runs}...")
        sim = SimpleQueueSimulation(lambda_rate, mu_rate, K)
        sim.run_simulation(max_time)
        stats = sim.get_statistics()
        results.append(stats)
    
    # Calcular promedios
    avg_results = {}
    for key in ['NS', 'TS', 'Nw', 'Tw', 'lambda_eff', 'blocking_prob']:
        avg_results[key] = sum(r[key] for r in results) / len(results)
    
    # Mostrar resultados
    print("\n" + "=" * 80)
    print("RESULTADOS COMPARATIVOS")
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
    print("ESTADÍSTICAS ADICIONALES")
    print("=" * 80)
    print(f"Tasa efectiva de llegada (teórica): {theoretical['lambda_eff']:.4f}")
    print(f"Tasa efectiva de llegada (simulada): {avg_results['lambda_eff']:.4f}")
    print(f"Probabilidad de bloqueo (simulada): {avg_results['blocking_prob']:.4f}")
    print(f"Utilización teórica (ρ): {theoretical['rho']:.4f}")
    
    return theoretical, avg_results, results

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
    max_time = 50000   # CAMBIAR: Tiempo máximo de simulación
    num_runs = 5       # CAMBIAR: Número de ejecuciones
    
    # Ejemplo de expresiones algebraicas:
    # lambda_rate = 100  # λ = 100 clientes/hora
    # mu_rate = 150      # μ = 150 clientes/hora
    # K = 10             # K = 10 (capacidad total)
    
    run_simple_simulation_and_compare(lambda_rate, mu_rate, K, max_time, num_runs)
