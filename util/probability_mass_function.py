
"""
This module implements a probability mass function from which single samples
can be drawn
"""

import numpy as np

class ProbabilityMassFunction:
    """
    The ProbabilityMassFunction (PMF) class is designed to allow for easy
    creation and use of a probability mass function.  Items and associated
    probability weights are given. Samples (items) can then be drawn from the
    pmf according to their relative weights.

    Parameters
    ----------
    items : list, optional
        The starting items in the PMF.
    weights : list-like of numeric, optional
        The relative weights of the items. The default is even weighting.

    Attributes
    ----------
    items : list
        The current items in the PMF
    normalized_weights : list-like numeric
        The probabilities of items
    """

    def __init__(self, items=None, weights=None):
        
        if items is None:
            items = []
        self.items = items
        self.weights = weights

 
    def add_item(self, new_item, new_weight=None):
        """Adds a single item to the PMF.

        Parameters
        ----------
        new_item
            The item to be added.
        new_weight : numeric
            (Optional) The weight associated with the item. The default is the
            average weight of the other items.
        """
        self.items.append(new_item)

    

    def draw_sample(self):
        """Draw a sample from the PMF

        Draw a random sample from the PMF according to the probabilities
        associated with weighting of items.

        Returns
        -------
            A single item
        """
        index = np.searchsorted(self._cumulative_weights, np.random.random())
        return self.items[index]
