"""
Mesa-based headless verification of M/M/1/K/Inf using a Model subclass.
"""

import math
import random
from typing import Dict, List, Tuple, Optional

try:
    # Common import path
    from mesa import Model  # type: ignore
except Exception:
    try:
        # Alternate import path in some Mesa versions
        from mesa.model import Model  # type: ignore
    except Exception as exc:  # pragma: no cover
        raise ImportError(
            "Mesa is required for mesa_mm1k.py. Install with: pip install -U \"mesa[rec]\""
        ) from exc


class MM1KModel(Model):
    """Headless event-driven M/M/1/K model implemented inside a Mesa Model."""

    def __init__(self, lambda_rate: float, mu_rate: float, capacity_k: int, max_time: float):
        super().__init__()
        self.lambda_rate = float(lambda_rate)
        self.mu_rate = float(mu_rate)
        self.capacity_k = int(capacity_k)
        self.max_time = float(max_time)

        # State
        self.current_time: float = 0.0
        self.queue: List[Dict] = []
        self.server_busy: bool = False
        self.server_customer: Optional[Dict] = None

        # Stats
        self.total_arrivals: int = 0
        self.total_departures: int = 0
        self.total_blocked: int = 0
        self.total_queue_time: float = 0.0
        self.total_system_time: float = 0.0

        # Event times
        self.next_arrival_time: float = 0.0
        self.next_service_completion_time: float = float("inf")

    # --- Event helpers ---
    def _exp(self, rate: float) -> float:
        return -math.log(1.0 - random.random()) / rate

    def _schedule_next_arrival(self) -> None:
        self.next_arrival_time = self.current_time + self._exp(self.lambda_rate)

    def _schedule_service_completion(self, customer: Dict) -> None:
        self.next_service_completion_time = self.current_time + self._exp(self.mu_rate)
        customer["service_start_time"] = self.current_time

    # --- Event handlers ---
    def _on_arrival(self) -> None:
        self.total_arrivals += 1
        customer = {
            "id": self.total_arrivals,
            "arrival_time": self.current_time,
            "service_start_time": None,
            "departure_time": None,
        }
        customers_in_system = len(self.queue) + (1 if self.server_busy else 0)
        if customers_in_system < self.capacity_k:
            if not self.server_busy:
                self.server_busy = True
                self.server_customer = customer
                self._schedule_service_completion(customer)
            else:
                self.queue.append(customer)
        else:
            self.total_blocked += 1
        self._schedule_next_arrival()

    def _on_service_complete(self) -> None:
        if self.server_busy and self.server_customer is not None:
            customer = self.server_customer
            customer["departure_time"] = self.current_time
            queue_time = customer["service_start_time"] - customer["arrival_time"]
            system_time = customer["departure_time"] - customer["arrival_time"]
            self.total_queue_time += queue_time
            self.total_system_time += system_time
            self.total_departures += 1
            self.server_busy = False
            self.server_customer = None
            self.next_service_completion_time = float("inf")
            if self.queue:
                next_customer = self.queue.pop(0)
                self.server_busy = True
                self.server_customer = next_customer
                self._schedule_service_completion(next_customer)

    # --- Run ---
    def step(self) -> None:  # type: ignore[override]
        # Advance to next event
        if self.next_arrival_time < self.next_service_completion_time:
            self.current_time = self.next_arrival_time
            self._on_arrival()
        else:
            self.current_time = self.next_service_completion_time
            self._on_service_complete()

    def run(self) -> None:
        # Initialize first arrival
        self._schedule_next_arrival()
        while self.current_time < self.max_time:
            self.step()

    def stats(self) -> Dict[str, float | int]:
        if self.total_departures == 0 or self.current_time <= 0:
            return {
                "NS": 0,
                "TS": 0,
                "Nw": 0,
                "Tw": 0,
                "lambda_eff": 0,
                "blocking_prob": 0,
                "total_arrivals": self.total_arrivals,
                "total_departures": self.total_departures,
                "total_blocked": self.total_blocked,
                "simulation_time": self.current_time,
            }
        lambda_eff = self.total_departures / self.current_time
        TS = self.total_system_time / self.total_departures
        Tw = self.total_queue_time / self.total_departures
        NS = lambda_eff * TS
        Nw = lambda_eff * Tw
        blocking_prob = (self.total_blocked / self.total_arrivals) if self.total_arrivals > 0 else 0
        return {
            "NS": NS,
            "TS": TS,
            "Nw": Nw,
            "Tw": Tw,
            "lambda_eff": lambda_eff,
            "blocking_prob": blocking_prob,
            "total_arrivals": self.total_arrivals,
            "total_departures": self.total_departures,
            "total_blocked": self.total_blocked,
            "simulation_time": self.current_time,
        }


def run_mesa_mm1k(lambda_rate: float, mu_rate: float, K: int, max_time: float, num_runs: int = 5) -> Tuple[Dict, Dict, List[Dict]]:
    """Run multiple Mesa replications and average results."""
    results: List[Dict] = []
    for _ in range(num_runs):
        model = MM1KModel(lambda_rate, mu_rate, K, max_time)
        model.run()
        results.append(model.stats())
    avg: Dict[str, float] = {}
    for key in ["NS", "TS", "Nw", "Tw", "lambda_eff", "blocking_prob"]:
        avg[key] = sum(float(r[key]) for r in results) / len(results)
    return avg, results[0], results
