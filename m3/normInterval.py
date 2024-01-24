# In a survey of 1200 randomly selected registered voters, 
# 348 were in favor of banning public smoking. Find the 95% 
# conﬁdence interval for the proportion of voters in favor 
# of banning public smoking.

import scipy.stats as st

# Let n be the number of voters surveyed.
n = 1200

# Let p be the proportion of voters that voted in favor
p = 348.0/1200.0

# The standard error is sqrt(p * (1-p)/n)
stderr = (p * (1 - p)/n) ** 0.5

print(st.norm.interval(0.95, p, stderr))

# In the Exam Scores data set, find a 99% confidence interval
# for the proportion of students who scores more than 90 in Exam 1.

import pandas as pd
import scipy.stats as st
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')

# Let n be the number of students who took Exam 1.
n = scores[['Exam1']].count()

# Let x be the total of all Exam 1 scores greater than 90
x = (scores[['Exam1']] > 90).values.sum()

# Let p be x/n, the proportion of all students that scored over 90 on Exam 1
# Multiplying by 1.0 is needed for correct floating point arithmetic
p = x/n*1.0

# The standard error is sqrt(p * (1-p)/n)
stderr = (p * (1 - p)/n) ** 0.5

print(st.norm.interval(0.99, p, stderr))