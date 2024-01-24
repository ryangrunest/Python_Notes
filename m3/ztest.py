from statsmodels.stats.weightstats import ztest
import pandas as pd
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')
print(ztest(x1 = scores['Exam1'],  value = 86))