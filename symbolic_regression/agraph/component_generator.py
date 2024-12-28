

from util.probability_mass_function import ProbabilityMassFunction

class ComponentGenerator:

    def __init__(self, 
        input_x_dimension,
        num_initial_load_statements=1, 
        constant_probability=None):

        self.input_x_dimension = input_x_dimension
        self._num_initial_load_statements = num_initial_load_statements

        self._operator_pmf = ProbabilityMassFunction()
        self._terminal_pmf = self._make_terminal_pdf(constant_probability)


    def _make_terminal_pdf(self, constant_probability):
        if constant_probability is None:
            terminal_weight = [1, self.input_x_dimension]
        else:
            terminal_weight = [constant_probability,
                               1.0 - constant_probability]
                               
        return ProbabilityMassFunction(items=[1, 0], weights=terminal_weight)


    def add_operator(self, operator_to_add, operator_weight=None):
        operator_number = operator_to_add
        self._operator_pmf.add_item(operator_number, operator_weight)

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
