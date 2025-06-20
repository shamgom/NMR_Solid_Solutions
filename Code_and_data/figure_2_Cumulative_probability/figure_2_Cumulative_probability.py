import matplotlib.pyplot as plt
import math

def calculate_binomial_coefficient(N, n):
    return math.factorial(N) / (math.factorial(n) * math.factorial(N - n))

def probability_function(N, n, x):
    return calculate_binomial_coefficient(N, n) * (x ** n) * ((1 - x) ** (N - n))

# Define the values of N and n
N = 100
n = 20

# Create a list of x values from 0 to 100 with increments of 1
x = list(range(101))

# Calculate the values of the function
y = [probability_function(N, n, 0.2) for n in x]

# Create the scatter plot
plt.scatter(x, y, c='blue', marker='o', s=5)  # c is the color, marker defines the style of the point, s is the size

# Add vertical lines
for xi, yi in zip(x, y):
    plt.plot([xi, xi], [0, yi], color='gray', linestyle='--', linewidth=0.5)

plt.xlabel('$n$', fontsize=14, fontstyle='italic')  # x-axis label
plt.ylabel('$P$$_n$', fontsize=14)  # y-axis label with subscript

# Adjust the font size of ticks
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Save the figure as a JPG file
plt.savefig('figure_2_Cumulative_probability.tiff', format='tiff')
plt.savefig('figure_2_Cumulative_probability.pdf', format='pdf')
plt.show()

