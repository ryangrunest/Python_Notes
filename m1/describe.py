# The DataFrame.describe() function generates a five-number summary. 
# Q1, the 25th percentile, is shown as 25%
# the median, the 50th percentile, is shown as 50% 
# Q3, the 75thth percentile, is shown as 75%.

import pandas as pd

list = [0, -6, 10, 5, 8, 2, -12, 11, -2]
scores = pd.DataFrame(list)

# Prints the summary for each exam
print(scores.describe())

# Prints the summary for Exam1 only
# print(scores[['Exam1']].describe())