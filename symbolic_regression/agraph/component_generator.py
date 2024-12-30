
import numpy as np
from util.probability_mass_function import ProbabilityMassFunction
from .operator_definitions import OPERATOR_NAMES

class ComponentGenerator:

    def __init__(self, 
        input_x_dimension,
        num_initial_load_statements=1, 
        terminal_probability=0.1,
        constant_probability=None):

        self.input_x_dimension = input_x_dimension
        self._num_initial_load_statements = num_initial_load_statements

        self._operator_pmf = ProbabilityMassFunction()
        self._terminal_pmf = self._make_terminal_pdf(constant_probability)

        self._random_command_function_pmf = self._make_random_command_pmf(terminal_probability)

    def _make_random_command_pmf(self, terminal_probability):
        command_weights = [terminal_probability,
                           1.0 - terminal_probability]
        return ProbabilityMassFunction(items=[self.random_terminal_command,
                                              self.random_operator_command],
                                       weights=command_weights)

    def random_operator_command(self, stack_location):

        return np.array([self.random_operator(),
                         self.random_operator_parameter(stack_location),
                         self.random_operator_parameter(stack_location)],
                        dtype=int)

    def random_operator(self):
        return self._operator_pmf.draw_sample()

    def _make_terminal_pdf(self, constant_probability):
        if constant_probability is None:
            terminal_weight = [1, self.input_x_dimension]
        else:
            terminal_weight = [constant_probability,
                               1.0 - constant_probability]

        return ProbabilityMassFunction(items=[1, 0], weights=terminal_weight)

    
    def random_terminal_parameter(self, terminal_number):
        if terminal_number == 0:
            param = np.random.randint(self.input_x_dimension)
        else:
            param = -1
        return param


    def add_operator(self, operator_to_add, operator_weight=None):
   
        if isinstance(operator_to_add, str):
            operator_number = self._get_operator_number_from_string(
                operator_to_add)
        else:
            operator_number = operator_to_add

        self._operator_pmf.add_item(operator_number, operator_weight)

    @staticmethod
    def _get_operator_number_from_string(operator_string):
        for operator_number, operator_names in OPERATOR_NAMES.items():
            if operator_string in operator_names:
                return operator_number
        raise ValueError(f"Could not find operator {operator_string}. ")


    @staticmethod
    def random_operator_parameter(stack_location):
        return np.random.randint(stack_location)    

    def random_terminal(self):
        return self._terminal_pmf.draw_sample()    

    def random_terminal_command(self, _=None):
   
        terminal = self.random_terminal()
        param = self.random_terminal_parameter(terminal)
        return np.array([terminal, param, param], dtype=int)


    def random_command(self, stack_location):
   
        if stack_location < self._num_initial_load_statements:
            return self.random_terminal_command(stack_location)
        return self._random_command_function_pmf.draw_sample()(stack_location)
