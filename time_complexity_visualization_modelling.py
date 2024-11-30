import numpy as np
import matplotlib.pyplot as plt
import math

# Generate input values
n = np.arange(1, 21)

# Define example functions
functions = {
    "O(n!)": np.array([math.factorial(x) for x in n]),
    "O(2^n)": 2**n,
    "O(n^2)": n**2,
    "O(n log n)": n * np.log(n),
    "O(n)": n,
    "O(log n)": np.log(n)
}

# Target functions
target_functions = {
    "O(n!)": np.array([math.factorial(x) for x in n]),
    "O(2^n)": 2**n,
    "O(n^2)": n**2,
    "O(n log n)": n * np.log(n),
    "O(n)": n,
    "O(log n)": np.log(n)
}

# Plotting
plt.figure(figsize=(14, 8))

# Plot the target functions
for name, values in target_functions.items():
    plt.plot(n, values, label=name, linestyle='dotted')

# Plot the example functions with different styles
for i, (name, values) in enumerate(functions.items()):
    distances = {}
    for t_name, t_values in target_functions.items():
        # Calculate Euclidean distance
        distance = np.linalg.norm(values - t_values)
        distances[t_name] = distance

    # Find the closest target function
    closest = min(distances, key=distances.get)

    # Plot the example function
    plt.plot(n, values, label=f"{name} (Closest: {closest})", linewidth=2)
    print(f"{name} is closest to {closest} with distance {distances[closest]}")

plt.xlabel('n')
plt.ylabel('Time Complexity')
plt.yscale('log')
plt.legend()
plt.title('Comparison of Time Complexities')
plt.grid(True)
plt.show()
