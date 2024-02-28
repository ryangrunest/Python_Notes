# Python-Practice 8.2.1: Using a chi-square goodness-of-fit test.
# The chisquare object from the scipy.stats library can be used to perform a chi-square goodness of fit test. Ex: a biologist is counting birds on the lake and comparing the distribution to last week's counts. The observed and expected counts are given in the table below.

# Calculates the chi-square statistic and $p$-value for alpha = 0.05 for the given observed and expected counts
statistic, pvalue = chisquare([61, 17, 11, 15, 6], f_exp=[55, 25.3, 13.2, 11, 5.5])

print(statistic)
print(pvalue)