import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, lambdify

def plot_function(func_str, x_min=-10, x_max=10, num_points=500):
    """Plots a mathematical function.

    Args:
        func_str: The function as a string (e.g., "x**2 + 2*x + 1").  
                  Supports basic mathematical operations and the variable 'x'.
        x_min: The minimum x-value for the plot.
        x_max: The maximum x-value for the plot.
        num_points: The number of points to generate for the plot.
    """
    try:
        # Use sympy to parse the function string and create a lambda function
        func = sympify(func_str)
        f = lambdify(func.free_symbols, func, modules=['numpy'])

        x = np.linspace(x_min, x_max, num_points)
        y = f(x)

        plt.figure(figsize=(10, 6)) # Adjust figure size if needed
        plt.plot(x, y)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title(f"Graph of f(x) = {func_str}")
        plt.grid(True)
        plt.show()

    except (SyntaxError, TypeError, NameError, ValueError) as e:
        print(f"Error: Invalid function input or parsing error: {e}")


if name == "main":
    func_input = input("Enter the function (e.g., x**2 + 2*x + 1): ")
    plot_function(func_input)