# The proportions_ztest() function can also perform a 
# z-test between two samples. The function requires the statsmodels.stats.proportion library to be imported, and takes two arrays, instead of two integers, as parameters. The first array is the number of individuals meeting some condition in each group, and the second array is the total number of individuals in each group.

# The function returns the 
# z-score and the two-tailed 
# p-value.

from statsmodels.stats.proportion import proportions_ztest
counts = [95, 125]
n = [5000, 5000]
print(proportions_ztest(counts, n))