# Python-Function 5.5.1: ols(), fit(), and summary().
# The ols() function performs ordinary linear regression, 
# and the fit() function fits the data to the regression line. 
# These functions require the statsmodels.formula.api library to be imported. 
# ols() takes two parameters. The first parameter is in the form 'Y ~ X', where Y is 
# the response variable and X is the predictor variable. 
# The second parameter is the dataset that contains the variables.

# The summary() function returns a summary including estimates for the parameters, 
# t-statistics, 
# p-values, and confidence intervals.

# All of the above functions require the statsmodels.formula.api library to be imported.

import pandas as pd
import statsmodels.formula.api as smf
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')

model = smf.ols('Exam4 ~ Exam2', scores).fit()
print(model.summary())