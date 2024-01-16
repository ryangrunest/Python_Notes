# The DataFrame.std() function is used to find the standard deviation, and the DataFrame.var() is used to find the variance.

import pandas as pd

# Loads the ExamScores dataset
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')

# Prints the standard deviation for each exam
print(scores.std())

# Prints the standard deviation for Exam1 only
print(scores[['Exam1']].std()) 

# Prints the variance for each exam
print(scores.var())

# Prints the variance for Exam1 only
print(scores[['Exam1']].var())