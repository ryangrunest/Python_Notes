import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Set the mean and standard deviation
mean = 5
std_dev = 2

# Generate data points for the x-axis (considering x >= -1)
x = np.linspace(-1, mean + 3*std_dev, 1000)

# Calculate the cumulative distribution function values
cdf_values = norm.cdf(x, loc=mean, scale=std_dev)

# Plot the CDF of the normal distribution
plt.plot(x, cdf_values, label='Cumulative Distribution Function (CDF)')

# Highlight the area for x >= -1
plt.fill_between(x, cdf_values, where=(x >= -1), alpha=0.3, color='purple', label='P(x >= -1)')

# Add labels and a legend
plt.xlabel('X')
plt.ylabel('Cumulative Probability')
plt.title('Normal Distribution CDF with Highlighted Area for x >= -1')
plt.legend()

# Show the plot
plt.show()
