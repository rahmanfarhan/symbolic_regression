"""Acyclic graph representation of an equation.


This module contains most of the code necessary for the representation of an
acyclic graph (linear stack) in symbolic regression.

Stack
-----

The stack is represented as Nx3 integer array. Where each row of the array
corresponds to a single command with form:

========  ===========  ===========
Node      Parameter 1  Parameter 2
========  ===========  ===========

Where the parameters are a reference to the result of previously executed
commands (referenced by row number in the stack). The result of the last (N'th)
command in the stack is the evaluation of the equation.

Note: Parameter values have special meaning for two of the nodes (0 and 1).

Nodes
-----

An integer to node mapping is how the command stack is parsed.
The current map is outlined below.

========  =======================================  =================
Node      Name                                     Math
========  =======================================  =================
0         load p1'th column of x                   :math:`x_{p1}`
1         load p1'th constant                      :math:`c_{p1}`
2         addition                                 :math:`p1 + p2`
3         subtraction                              :math:`p1 - p2`
4         multiplication                           :math:`p1 - p2`
5         division (not divide-by-zero protected)  :math:`p1 / p2`
6         sine                                     :math:`sin(p1)`
7         cosine                                   :math:`cos(p1)`
8         exponential                              :math:`exp(p1)`
9         logarithm                                :math:`log(|p1|)`
10        power                                    :math:`p1^{p2}`
11        absolute value                           :math:`|p1|`
12        square root                              :math:`sqrt(|p1|)`
13        safe                                     :math:`|p1|^{p2}`
14        hyperbolic sine                          :math:`sinh(p1)`
15        hyperbolic cosine                        :math:`cosh(p1)`
========  =======================================  =================
"""


import numpy as np

class AGraph():

    def __init__(self, equation=None):
        self._init_command_array_and_const(equation)

    def _init_command_array_and_const(self, equation):
        if equation is None:
            self._command_array = np.empty([0, 3], dtype=int)

            self._simplified_command_array = np.empty([0, 3], dtype=int)
            self._simplified_constants = []

            self._needs_opt = False
            self._modified = False