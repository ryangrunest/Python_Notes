# The MultipleComparison() function take the data frame column that contains the values and the data frame column that contains the levels as inputs and builds the models. The tukeyhsd() function displays the 
#  Tukey's confidence intervals. The statsmodels.stats.multicomp library must be imported to use these functions.

import pandas as pd
from statsmodels.stats.multicomp import (pairwise_tukeyhsd, MultiComparison)
df = pd.read_csv('http://data-analytics.zybooks.com/ExamScoresGrouped.csv')
mod = MultiComparison(df['Scores'], df['Exam'])
print(mod.tukeyhsd())