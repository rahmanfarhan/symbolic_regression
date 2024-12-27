
from .evolutionary_optimizer import EvolutionaryOptimizer

class Island(EvolutionaryOptimizer):

    def __init__(self, evolutionary_algo, generator, population_size, hall_of_fame):
        super().__init__()
        self._generator = generator
        self._population_size = population_size
        self._ea = evolutionary_algo

        self.population = [generator() for _ in range(population_size)]

    