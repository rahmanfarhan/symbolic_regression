import numpy as np
from .agraph import AGraph as pyAGraph

class AGraphGenerator():
    
    def __init__(self, agraph_size, component_generator, use_python=False):
        
        self.agraph_size = agraph_size #same as stack_size
        self.component_generator = component_generator
        if use_python:
            self._backend_generator_function = self._python_generator_function

    def __call__(self):
        individual = self._backend_generator_function()
        individual.command_array = self._create_command_array()
        return individual

    def _python_generator_function(self):
        return pyAGraph()

    def _create_command_array(self):
        command_array = np.empty((self.agraph_size, 3), dtype=int)
        
        for i in range(self.agraph_size):
            command_array[i] = self.component_generator.random_command(i)
        return command_array