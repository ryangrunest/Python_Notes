
# The proportions_ztest(count, nobs, value, prop_var = value) function is used to perform a one-sample 
# -test for proportions. The function requires the statsmodels.stats.proportion library to be imported, 
# and takes four inputs. The first input count is the number of observations meeting some condition, 
# the second input nobs is the total number of observations, 
# the third input is the hypothesized value of the population proportion, 
# and the fourth is the hypothesized value of the population proportion which is used to 
# calculate the variance of the estimate.

# The function returns the z-score and the two-tailed p-value.

from statsmodels.stats.proportion import proportions_ztest
counts = 31
nobs = 50
value = 0.50
print(proportions_ztest(counts, nobs, value, prop_var=value))