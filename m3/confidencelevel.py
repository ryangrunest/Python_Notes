import scipy.stats as stats
import math

# Given data set
data_set = [71, 73, 69, 65, 70, 75, 75]

# Calculate sample mean and standard deviation
sample_mean = sum(data_set) / len(data_set)
print("mean", sample_mean)

sample_std = stats.tstd(data_set)

# Specify confidence level and degrees of freedom (for t-distribution)
confidence_level = 0.99
degrees_of_freedom = len(data_set) - 1

# Calculate the t-score for the given confidence level
t_score = stats.t.ppf((1 + confidence_level) / 2, degrees_of_freedom)

# Calculate margin of error
margin_of_error = t_score * (sample_std / math.sqrt(len(data_set)))

print('margin of error', margin_of_error)