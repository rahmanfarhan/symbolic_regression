
from .agraph import AGraph as pyAGraph

class AGraphGenerator():
    
    def __init__(self, component_generator, use_python=False):
        
        self.component_generator = component_generator
        if use_python:
            self._backend_generator_function = self._python_generator_function


    def _python_generator_function(self):
        return pyAGraph()