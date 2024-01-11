import pandas as pd

# Loads the ExamScores dataset
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')

# Prints the mode(s) for each exam
print(scores.mode())

# Prints the mode(s) for Exam1 only
print(scores[['Exam1']].mode())