import os
from evolutionary_algorithms.age_fitness import AgeFitnessEA
from stats.pareto_front import ParetoFront

class SymbolicRegressor():
    def __init__(
        self, 
        population_size=500, 
        stack_size=20, 
        use_simplification=True,
        evolutionary_algorithm=None):
        
        self.population_size = population_size
        self.stack_size = stack_size
        self.use_simplification = use_simplification
        
        if evolutionary_algorithm is None:
            evolutionary_algorithm = AgeFitnessEA
        self.evolutionary_algorithm = evolutionary_algorithm


    def _get_archipelago(self, X, y, n_processes): 

        if self.evolutionary_algorithm == AgeFitnessEA:
            evo_alg = self.evolutionary_algorithm()
       
        hof = ParetoFront()

        island = self._make_island(len(X), evo_alg, hof) 
        return island
        pass

    def fit(self, X, y):

        n_cpus = int(os.environ.get("OMP_NUM_THREADS", "0"))
        self.archipelago = self._get_archipelago(X, y, n_cpus)
        
        pass

    def get_best_individual(self):
        pass