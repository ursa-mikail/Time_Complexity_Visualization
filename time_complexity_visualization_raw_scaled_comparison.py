import numpy as np
import matplotlib.pyplot as plt
import random
import time
import math

def compare_complexity(custom_func, n_range):
    # Generate input values
    n = np.arange(1, n_range + 1)

    # Compute the values for the custom function
    custom_values = custom_func(n)

    # Define the target O() functions with distinct colors
    target_functions = {
        "O(n!)": np.array([math.factorial(min(x, 20)) for x in n], dtype=float),
        "O(2^n)": 2**n,
        "O(n^2)": n**2,
        "O(n log n)": n * np.log(n),
        "O(n)": n,
        "O(log n)": np.log(n)
    }

    # Plotting
    plt.figure(figsize=(14, 8))

    # Plot the target functions
    colors = {
        "O(n!)": 'cyan',
        "O(2^n)": 'magenta',
        "O(n^2)": 'yellow',
        "O(n log n)": 'orange',
        "O(n)": 'purple',
        "O(log n)": 'brown'
    }

    for name, values in target_functions.items():
        plt.plot(n, values, label=name, linestyle='dotted', color=colors[name])

    # Calculate distances and find the closest target function
    distances = {}
    for t_name, t_values in target_functions.items():
        # Calculate mean squared error
        distance = np.mean((custom_values - t_values)**2)
        distances[t_name] = distance

    # Find the closest target function
    closest = min(distances, key=distances.get)

    # Plot the custom function
    plt.plot(n, custom_values, label="Custom Function", linewidth=5, linestyle='dotted', color='red')

    # Highlight the closest target function in green
    plt.plot(n, target_functions[closest], label=f"Closest: {closest}", linewidth=2, color='green')

    plt.xlabel('n')
    plt.ylabel('Value (Time Complexity)')
    plt.title('Comparison of Time Complexities (Raw Scale)')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Print the distances for reference
    for name, distance in distances.items():
        print(f"Distance to {name}: {distance}")
    print(f"Custom function is closest to {closest} with distance {distances[closest]}")

def example_n_factorial(n):
    # Limit factorials to a reasonable range to prevent overflow
    result = []
    for i in n:
        # Limit to smaller values to prevent extreme growth
        fact_result = math.factorial(min(i, 20))
        result.append(fact_result)
    return np.array(result, dtype=float)

# Example of a custom function with O(n^2) complexity
def example_n_squared(n):
    result = []
    for i in n:
        sum = 0
        for j in range(i):
            for k in range(i):
                sum += 1
        result.append(sum)
    return np.array(result)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example of a custom function with O(2^n) complexity
def example_2_pow_n(n):
    result = []
    for i in n:
        sum = fibonacci(i)
        result.append(sum)
    return np.array(result)

# List of mystery functions
mystery_functions = [example_2_pow_n, example_n_squared, example_n_factorial]

# Select a random function from the list
chosen_index = random.randint(0, len(mystery_functions) - 1)
chosen_function = mystery_functions[chosen_index]
print(f"chosen_function: {chosen_function.__name__}")

time_start = time.time()  # Record the start time
n_range = 20  # Reduced range to prevent extreme values

# Call the compare_complexity function with the chosen function
compare_complexity(chosen_function, n_range)

time_end = time.time()  # Record the end time
time_elapsed = time_end - time_start  # Calculate the elapsed time
print(f"Time elapsed: {time_elapsed} seconds")


"""
chosen_function: example_n_squared

Distance to O(n!): 2.9669254145927475e+35
Distance to O(2^n): 73224684701.3
Distance to O(n^2): 0.0
Distance to O(n log n): 24970.45825811329
Distance to O(n): 31866.8
Distance to O(log n): 35367.35226670491
Custom function is closest to O(n^2) with distance 0.0
Time elapsed: 0.34624147415161133 seconds
"""