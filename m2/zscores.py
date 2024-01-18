# The norm.ppf() and norm.isf() functions are used to convert percentiles to 
# z-scores. The scipy.stats library must be imported to use these functions.
# norm.ppf(p, mean, sd) returns the critical 
# -score for which the probability of 
#  being below that 
# -score is p, for a normal distribution with the specified mean and standard deviation.

import scipy.stats as st

# For a normal distribution, if the mean is 0 and 
# the standard deviation is 1, what is z* if P(z < z*) = 0.135?
print(st.norm.ppf(0.135, 0, 1))


# norm.isf(p, mean, sd) returns the critical 
# z-score for which the probability of z being above that z-score is p, for a normal distribution with the specified mean and standard deviation.

# For a normal distribution, if the mean is 0 and 
# the standard deviation is 1, what is z* if P(z > z*) = 0.405?
print(st.norm.isf(0.405, 0, 1))



# Both norm.ppf() and norm.isf() can also be used with non-standard normal distributions.

# For a normal distribution, if the mean is 55 and 
# the standard deviation is 7.5, what is x* if P(x < x*) = 0.8247?
print(st.norm.ppf(0.8247, 55, 7.5))

# For a normal distribution, if the mean is 55 and 
# the standard deviation is 7.5, what is x* if P(x > x*) = 0.95?
print(st.norm.isf(0.95, 55, 7.5))




# EXAMPLE QUESTIONS
# The GRE (Graduate Record Exam) scores for both verbal and quantitative reasoning are approximately normally distributed and scaled to have mean 150
#  with standard deviation of 8.75.

# Below what score do 40% of all scores fall? Type as: #.###
print(st.norm.ppf(0.4, 150, 8.75))

# Above what score do 20% of all scores fall? Type as: #.###
print(st.norm.isf(0.2, 150, 8.75))