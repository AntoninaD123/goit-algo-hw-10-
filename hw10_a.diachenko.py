#task 1

from pulp import LpMaximize, LpProblem, LpVariable, value

# Define the problem
model = LpProblem("Production_Optimization", LpMaximize)

# Define decision variables (number of products)
lemonade = LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = LpVariable('FruitJuice', lowBound=0, cat='Integer')

# Objective function: maximize total production
model += lemonade + fruit_juice, "Total_Products"

# Constraints
model += 2*lemonade + 1*fruit_juice <= 100, "Water"
model += 1*lemonade <= 50, "Sugar"
model += 1*lemonade <= 30, "Lemon_Juice"
model += 2*fruit_juice <= 40, "Fruit_Puree"

# Solve the problem
model.solve()

# Results
print("Optimal production plan:")
print(f"Lemonade: {int(lemonade.value())} units")
print(f"Fruit Juice: {int(fruit_juice.value())} units")
print(f"Total products: {int(value(model.objective))}")


#task 2
import random

# Function to integrate
def f(x):
    return x**2

# Monte Carlo parameters
a = 0   # lower bound
b = 2   # upper bound
N = 100000  # number of random points

# Generate random points and evaluate
points = [random.uniform(a, b) for _ in range(N)]
values = [f(x) for x in points]

# Estimate integral
integral_estimate = (b - a) * sum(values) / N
print(f"Estimated integral of f(x)=x^2 from {a} to {b} using Monte Carlo: {integral_estimate}")

# For comparison: analytical solution
analytical_integral = (b**3 - a**3)/3
print(f"Analytical integral: {analytical_integral}")
