# Python-Function 5.1.1: linregress(x,y).
# The intercept parameter estimator 
# b0 and the slope parameter estimator 
# b1 can be obtained by using the linregress(x,y) function, which takes in two arrays of equal length as input and returns 
# b0, b1, the correlation coefficient r, the 
# p-value for the correlation coefficient 
# t-test, and the corresponding standard error. The linregress(x,y) function uses the scipy.stats library.

# The numpy library is imported to build two arrays
import numpy as np
import scipy.stats as st

x = np.array([0, 3, 7, 10])
y = np.array([5, 5, 27, 31])

print(st.linregress(x,y))