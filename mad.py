# The DataFrame.mad() function is used to find the mean absolute deviation.

import pandas as pd

# Loads the ExamScores dataset
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')

# Prints the mean absolute deviation of all scores
print(scores.mad())

# Prints the mean absolute deviation of Exam 1
print(scores['Exam1'].mad())