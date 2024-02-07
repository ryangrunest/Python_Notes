# The ztest(x1, x2, value = 0) function can also be used to perform a two-sample z-test for means.
# However, the value parameter should be set to 0. The function requires the statsmodels.stats.weightstats 
# library to be imported and takes two inputs. The first input x1 is an array containing sample observations 
# from one population and the second input is also an array containing sample observations from another population.
# The function returns the z-score and the two-tailed p-value.

from statsmodels.stats.weightstats import ztest
sample1 = [21, 28, 40, 55, 58, 60]
sample2 = [13, 29, 50, 55, 71, 90]
print(ztest(x1 = sample1, x2 = sample2))