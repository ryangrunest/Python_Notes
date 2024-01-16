import pandas as pd
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')

# Calculating the range by subtracting the minimum from the maximum
score_range = scores.max() - scores.min()
print(score_range)

# Defining a function that can be used repeatedly
def range_of_scores(x):
  return x.max() - x.min()
print(range_of_scores(scores))
print(range_of_scores(scores[['Exam1']]))
print(range_of_scores(scores[['Exam2']]))
print(range_of_scores(scores[['Exam4']]))