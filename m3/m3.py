import numpy as np
from scipy import stats

# Step 3: Collect and Analyze Data
# Let's assume you have the following sample data:
sample_data = np.array([2.88, 3.00, 2.27, 2.16, 2.42, 3.20, 2.76, 2.65, 2.63, 2.77, 1.76, 2.58, 2.46, 1.82, 4.07, 2.44, 2.21, 3.36, 2.83, 2.71, 3.44, 1.20, 3.03, 2.02, 2.36, 3.18, 3.20, 2.45, 1.86, 1.63, 1.83, 2.41, 1.94, 3.05, 2.02, 2.41, 2.00, 2.41, 2.10, 2.21, 2.09, 2.49, 1.89, 2.30, 3.84, 3.16, 2.35, 2.63, 2.45, 3.01])

# Step 4: Calculate Sample Statistics
sample_mean = np.mean(sample_data)
sample_std = np.std(sample_data, ddof=1)  # ddof=1 for sample standard deviation
sample_size = len(sample_data)

# Step 5: Set Hypotheses and Significance Level
hypothesized_mean = 2.30  # hypothesized population mean
alpha = 0.01

# Step 6: Perform One-Sample Z-Test
z_stat, p_value = stats.ttest_1samp(sample_data, popmean=hypothesized_mean)

# Determine Critical Region
critical_value = stats.t.ppf(1 - alpha, df=sample_size - 1)  # One-tailed critical value
upper_critical_limit = hypothesized_mean + critical_value * (sample_std / np.sqrt(sample_size))

# Output Results
print(f"Sample Mean: {sample_mean:.4f}")
print(f"Z-Statistic: {z_stat:.4f}")
print(f"P-Value: {p_value:.4f}")
print(f"Critical Region: (>{upper_critical_limit:.4f})")

# Draw Conclusions
if z_stat > critical_value:
    print("Reject the null hypothesis. There is evidence that the average diameter is greater than 2.30 cm.")
else:
    print("Fail to reject the null hypothesis. There is not enough evidence to suggest that the average diameter is greater than 2.30 cm.")