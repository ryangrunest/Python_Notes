# Python-Function 2.5.1: t.cdf() and t.sf().
# The t.cdf() and t.sf() functions are used to find probabilities related to the 
# t-distribution. The scipy.stats library must be imported to use these functions.

# t.cdf(t, df, mean, sd) returns the probability of 
#  t being less than the critical value 
#  t for a 
#  t-distribution with the specified degrees of freedom, mean, and standard deviation.

import scipy.stats as st

# For a t-distribution, if the degrees of freedom is 30, the mean is 0,
# and the standard deviation is 1, what is P(t < -0.25)?
print(st.t.cdf(-0.25, 30, 0, 1))

# For a t-distribution, if the degrees of freedom is 30, the mean is 0,
# and the standard deviation is 1, what is P(t < 1.5)?
print(st.t.cdf(1.5, 30, 0, 1))

# t.sf(t, df, mean, sd) returns the probability of 
#  t being greater than the critical value 
#  t for a 
# t-distribution with the specified degrees of freedom, mean, and standard deviation.


import scipy.stats as st

# For a t-distribution, if the degrees of freedom is 30, the mean is 0,
# and the standard deviation is 1, what is P(t > -0.25)?
print(st.t.sf(-0.25, 30, 0, 1))

# For a t-distribution, if the degrees of freedom is 30, the mean is 0,
# and the standard deviation is 1, what is P(t > 1.5)?
print(st.t.sf(1.5, 30, 0, 1))


# To find the probability between two critical values, the difference between the two probabilities is calculated.

import scipy.stats as st

# For a t-distribution, if the degrees of freedom is 30, the mean is 0,
# and the standard deviation is 1, what is P(-0.25 < t < 1.5)?
print(st.t.cdf(1.5, 30, 0, 1) - st.t.cdf(-0.25, 30, 0, 1))

# For a t-distribution, if the degrees of freedom is 30, the mean is 0,
# and the standard deviation is 1, what is P(1.5 < t < 2.85)?
print(st.t.cdf(2.85, 30, 0, 1) - st.t.cdf(1.5, 30, 0, 1))

# Both t.cdf() and t.sf() can also be used for 
# t-distributions with different degrees of freedom and when the mean is not 
#  0 or the standard deviation is not 1.

import scipy.stats as st

# For a t-distribution, if the degrees of freedom is 59, the mean is 55,
# and the standard deviation is 7.5, what is P(t < 62)?
print(st.t.cdf(62, 59, 55, 7.5))

# For a t-distribution, if the degrees of freedom is 34, the mean is 55,
# and the standard deviation is 7.5, what is P(t > 51)?
print(st.t.sf(51, 34, 55, 7.5))

# For a t-distribution, if the degrees of freedom is 59, the mean is 55,
# and the standard deviation is 7.5, what is P(49 < t < 60)?
print(st.t.cdf(60, 59, 55, 7.5) - st.t.cdf(49, 59, 55, 7.5))




# The t.ppf() and t.isf() functions are used to convert percentiles to 
# t-statistics. The scipy.stats library must be imported to use these functions.

# t.ppf(p, df, mean, sd) returns the critical 
# t-statistic for which the probability of 
#  t being below that 
# t -score is p, for a 
# t -distribution with the specified degrees of freedom, mean, and standard deviation.

import scipy.stats as st

# For a t-distribution, if the degrees of freedom is 49, the mean is 0 and 
# the standard deviation is 1, what is t* if P(t < t*) = 0.135?
print(st.t.ppf(0.135, 49, 0, 1))




# t.isf(p, df, mean, sd) returns the critical 
# t-statistic for which the probability of 
#  t being above that 
# t-score is p, for a 
# t-distribution with the specified degrees of freedom, mean, and standard deviation.

import scipy.stats as st

# For a t-distribution, if the degrees of freedom is 49, the mean is 0 and 
# the standard deviation is 1, what is t* if P(t > t*) = 0.405?
print(st.t.isf(0.405, 49, 0, 1))



# Both t.ppf() and t.isf() can also be used with non-standard 
# t-distributions.

import scipy.stats as st

# For a t-distribution, if the degrees of freedom is 24, the mean is 55 and 
# the standard deviation is 7.5, what is t* if P(t < t*) = 0.8247?
print(st.t.ppf(0.8247, 24, 55, 7.5))

# For a t-distribution, if the degrees of freedom is 24, the mean is 55 and 
# the standard deviation is 7.5, what is t* if P(t > t*) = 0.95?
print(st.t.isf(0.95, 24, 55, 7.5))



# EXAMPLE QUESTION
# Find the 25th percentile of the t-distribution with 30 degrees of freedom. Type as #.###
print(st.t.ppf(0.25, 30))


# EXAMPLE QUESTION
# Find the 60th percentile of the t-distribution with 4degrees of freedom. Type as #.###
print(st.t.ppf(0.6, 4))