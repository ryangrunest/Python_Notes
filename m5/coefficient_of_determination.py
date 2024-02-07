# Python-Practice 5.3.1: Coefficient of determination.
# Another way to find the regression coefficients is to use the statsmodels package. 
# The code ols('y ~ x', data=dataframe).fit() where y is the dataframe column that represents
# the response variable and x is the dataframe column that represents the predictor variable. 
# The output gives other quantities including the coefficient of determination.

# The necessary packages are imported
import pandas as pd
from statsmodels.formula.api import ols

# The ExamScores dataset is loaded
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')

# Creates a linear regression model
results = ols('Exam4 ~ Exam1', data=scores).fit()

# Prints the results
print(results.summary())


# The explained and unexplained variance can be obtained from the analysis of variance table created using the code below.

# The necessary packages are imported
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# The ExamScores dataset is loaded
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')

# Creates a linear regression model
results = ols('Exam4 ~ Exam1', data=scores).fit()

# Creates an analysis of variance table
aov_table = sm.stats.anova_lm(results, typ=2)

# Prints the analysis of variance table
print(aov_table)