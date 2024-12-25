import numpy as np
import matplotlib.pyplot as plt
from bingo.symbolic_regression.symbolic_regressor import SymbolicRegressor

X_0 = np.linspace(-10, 10, num=30).reshape((-1, 1))
X = np.array(X_0)
y = 5.0 * X_0 ** 2 + 3.5 * X_0

plt.scatter(X, y)
plt.xlabel("X_0")
plt.ylabel("y")
plt.title("Training Data")
plt.show()

regressor = SymbolicRegressor(population_size=500, stack_size=20,
                              use_simplification=True)

regressor.fit(X, y)

best_individual = regressor.get_best_individual()
print("best individual is:", best_individual)

