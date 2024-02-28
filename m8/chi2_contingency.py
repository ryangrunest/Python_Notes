# Python-Practice 8.2.2: Chi-squared test of independence.
# The chi2_contingency object from the scipy.stats library can be used to perform a chi-square goodness of fit test. Conducting the chi-square test for independence requires first constructing a contingency table. An example using the parole data is shown below. Is there an association between a punishment record while in prison and success or failure while in prison?

import numpy as np
from scipy.stats import chi2_contingency

# Construct a contingency table
parole = np.array([[405,1422], [240,470], [151,275]])