# Python-Practice 5.5.1: Using ANOVA to test the correlation between two variables.
# The ols() function takes two parameters, 'Y ~ X1' where Y is the response variable 
# and X1 is a predictor variable, and a data frame. The sm.stats.anova_lm command takes in 
# a linear model and an ANOVA type as parameters and outputs an ANOVA table. 
# The different types of ANOVA are beyond the scope of this material. 
# To give the correct output, the parameter for the ANOVA type, denoted as typ, is set to 2.

# In the code below, Exam4 is the response variable and Exam1 is the predictor variable.

from statsmodels.formula.api import ols
import statsmodels.api as sm
import pandas as pd
df=pd.read_csv("http://data-analytics.zybooks.com/ExamScores.csv")
mod = ols('Exam4 ~ Exam1',df).fit()
print(sm.stats.anova_lm(mod, typ=2))