# Python-Practice 7.1.1: Multiple regression models.
# Consider the body fat dataset and a model where the response variable 
# Y is percent body fat and the predictor variables 
# X1 = triceps skinfold thickness (mm) and 
# X2 = midarm circumference (cm). The model is constructed using the code below.

import pandas as pd
from statsmodels.formula.api import ols

fat = pd.read_csv('https://static-resources.zybooks.com/static/fat.csv')

Y = fat['body_fat_percent']

m12 = ols('Y ~ triceps_skinfold_thickness_mm + midarm_circumference_cm', data = fat).fit()
print(m12.summary())