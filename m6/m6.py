# The mplot3d toolkit of matplotlib allows plotting of 3D objects such as scatterplots and 2D projections.

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("http://data-analytics.zybooks.com/Cars.csv")

fig = plt.figure()

#mplot3d is needed for projection='3d'
ax = fig.add_subplot(111, projection='3d')

ax.scatter(df['Speed'], df['Quality'], df['Angle'], c='b', marker='o')

ax.set_xlabel('Speed, X1')
ax.set_ylabel('Angle, X2')
ax.set_zlabel('Quality, Y')

plt.show()



# <------->

# Multiple Regression using Python 

# The body fat dataset gives the amount of body fat, the triceps skinfold circumference, the midarm circumference, and the thigh circumference of 
#  20 research subjects. Suppose a researcher wishes to use multiple regression to model the linear relationship between the amount of body fat for an individual and these body measurements. Let 
#  Y = body fat be the response variable and 
#  X1 = triceps skinfold circumference, 
#  X2 = midarm circumference, and 
#  X3 = thigh circumference be the three predictor variables.

# Similar to simple linear regression, ols(), fit(), and summary() are used to perform multiple regression, fit the data to the regression line, and display a summary. All of these functions require the statsmodels.formula.api module to be imported.

# To perform multiple regression, the predictor variables are joined with + in the ols() function. Finally, the fit() method is used.

import pandas as pd
import statsmodels.formula.api as sms

fat = pd.read_csv('https://static-resources.zybooks.com/static/fat.csv')

# Response variable
Y = fat['body_fat_percent']

# Generates the linear regression model
# Multiple predictor variables are joined with +
model = sms.ols('Y ~ triceps_skinfold_thickness_mm + midarm_circumference_cm + thigh_circumference_cm', data = fat).fit()

# Prints the summary
print(model.summary())


# <------>

# Multiple Regression Residuals

# The model object generated by statsmodels also contains the fitted values and residuals for each sample. To display the fitted values, the fittedvalues property of the model is called.

import pandas as pd
import statsmodels.formula.api as sms

fat = pd.read_csv('https://static-resources.zybooks.com/static/fat.csv')

# Response variable
Y = fat['body_fat_percent']

# Generates the linear regression model
# Multiple predictor variables are joined with +
model = sms.ols('Y ~ triceps_skinfold_thickness_mm + midarm_circumference_cm + thigh_circumference_cm', data = fat).fit()

# Prints a list of the fitted values for each sample
print(model.fittedvalues)

# To display the residuals, the resid property of the model is called.

# Prints a list of the residuals for each sample
print(model.resid)


# <------>

# Python-Practice 6.2.1: Residual plots.

import pandas as pd
import statsmodels.formula.api as sms
import matplotlib.pyplot as plt

fat = pd.read_csv('https://static-resources.zybooks.com/static/fat.csv')

# Response variable
Y = fat['body_fat_percent']

# Generates the linear regression model
# Multiple predictor variables are joined with +
model = sms.ols('Y ~ triceps_skinfold_thickness_mm + midarm_circumference_cm + thigh_circumference_cm', data = fat).fit()

plt.figure(figsize = (20, 16))
plt.tight_layout()

plt.subplot(2, 2, 1)
plt.scatter(x = fat['triceps_skinfold_thickness_mm'], y = model.resid, color = 'blue', edgecolor = 'k')
xmin = min(fat['triceps_skinfold_thickness_mm'])
xmax = max(fat['triceps_skinfold_thickness_mm'])
plt.hlines(y = 0, xmin = xmin, xmax = xmax, color = 'red', linestyle = '--')
plt.xlabel('$X_1$', fontsize = 16)
plt.ylabel('Residuals', fontsize = 16)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.title('$X_1$ vs. residuals', fontsize = 24)

plt.subplot(2, 2, 2)
plt.scatter(x = fat['midarm_circumference_cm'], y = model.resid, color = 'blue', edgecolor = 'k')
xmin = min(fat['midarm_circumference_cm'])
xmax = max(fat['midarm_circumference_cm'])
plt.hlines(y = 0, xmin = xmin, xmax = xmax, color = 'red', linestyle = '--')
plt.xlabel('$X_2$', fontsize = 16)
plt.ylabel('Residuals', fontsize = 16)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.title('$X_2$ vs. residuals', fontsize = 24)

plt.subplot(2, 2, 3)
plt.scatter(x = fat['thigh_circumference_cm'], y = model.resid, color = 'blue', edgecolor = 'k')
xmin = min(fat['thigh_circumference_cm'])
xmax = max(fat['thigh_circumference_cm'])
plt.hlines(y = 0, xmin = xmin, xmax = xmax, color = 'red', linestyle = '--')
plt.xlabel('$X_3$', fontsize = 16)
plt.ylabel('Residuals', fontsize = 16)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.title('$X_3$ vs. residuals', fontsize = 24)

plt.subplot(2, 2, 4)
plt.scatter(x = model.fittedvalues, y = model.resid, color = 'blue', edgecolor = 'k')
xmin = min(Y)
xmax = max(Y)
plt.hlines(y = 0, xmin = xmin, xmax = xmax, color = 'red', linestyle = '--')
plt.xlabel('Fitted values', fontsize = 16)
plt.ylabel('Residuals', fontsize = 16)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.title('Fitted values vs. residuals', fontsize = 24)
plt.show()


# <------>

# Python-Practice 6.2.2: qqplot().
# The qqplot method is used to generate a Q-Q plot.

import pandas as pd
import statsmodels.graphics.gofplots as smg
import statsmodels.formula.api as sms
import matplotlib.pyplot as plt

fat = pd.read_csv('https://static-resources.zybooks.com/static/fat.csv')

# Response variable
Y = fat['body_fat_percent']

# Generates the linear regression model
# Multiple predictor variables are joined with +
model = sms.ols('Y ~ triceps_skinfold_thickness_mm + midarm_circumference_cm + thigh_circumference_cm', data = fat).fit()

plt.figure(figsize = (8 ,5))
plt.subplot(1, 2, 1)
fig = smg.qqplot(model.resid, line = '45', fit = 'True')

plt.xlabel('Theoretical quantiles')
plt.ylabel('Sample quantiles')
plt.title('Q-Q plot of normalized residuals')
plt.show()

# <----->
# Python-Practice 6.3.1: Coefficient of multiple determination.
# Consider the body fat dataset and a model where the response variable 
# Y is percent body fat and the predictor variable 
# X1 is triceps skinfold thickness in millimeters. The model is constructed using the code below.

# R-squared: 0.711, which means that 
# 71.1% of the variance in percent body fat can be explained by the variance in triceps skinfold thickness.
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

fat = pd.read_csv('https://static-resources.zybooks.com/static/fat.csv')

# Response variable
Y = fat['body_fat_percent']

m01 = ols('Y ~ triceps_skinfold_thickness_mm', data = fat).fit()
print(m01.summary())


# <------>


