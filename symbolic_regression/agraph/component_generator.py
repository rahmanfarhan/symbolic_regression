

from util.probability_mass_function import ProbabilityMassFunction

class ComponentGenerator:

    def __init__(self, input_x_dimension,num_initial_load_statements=1):
        self.input_x_dimension = input_x_dimension
        self._num_initial_load_statements = num_initial_load_statements

        self._operator_pmf = ProbabilityMassFunction()

    
    def add_operator(self, operator_to_add, operator_weight=None):
        """Add an operator number to the set of possible operators

        Parameters
        ----------
        operator_to_add : int, str
            operator integer code (e.g. 2, 3) defined in Agraph operator maps
            or an operator string description (e.g. "+", "addition")
        operator_weight : number
                          relative weight of operator probability
        """
 
        operator_number = operator_to_add

        self._operator_pmf.add_item(operator_number, operator_weight)

    def random_terminal_command(self, _=None):
   
        terminal = self.random_terminal()
        param = self.random_terminal_parameter(terminal)
        return np.array([terminal, param, param], dtype=int)


    def random_command(self, stack_location):
   
        if stack_location < self._num_initial_load_statements:
            return self.random_terminal_command(stack_location)
        return self._random_command_function_pmf.draw_sample()(stack_location)
