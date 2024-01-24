import scipy.stats as st
import pandas as pd

n = 100

# Degrees of freedom is number of samples minus 1
df = n - 1

mean = 219

# The standard error is standard deviation/sqrt(number of samples)
stderr = 35.0/(n ** 0.5)

print(st.t.interval(0.95, df, mean, stderr))

# Import ExamScores.csv

scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')

# Let n be the number of students who took Exam 1.
n = scores[['Exam1']].count()

# Degrees of freedom is number of samples minus 1
df = n - 1

# The mean of Exam1 scores are obtained
mean = scores[['Exam1']].mean()

# The standard error is standard deviation/sqrt(number of samples)
stdev = scores[['Exam1']].std()
stderr = stdev/(n ** 0.5)

print(st.t.interval(0.95, df, mean, stderr))