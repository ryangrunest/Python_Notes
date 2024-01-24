# The scipy.stats.ttest_1samp(a, popmean) function takes in an array or a column of a DataFrame and the hypothesized population mean as inputs and gives the 
# -statistic and two-tailed 
# -value as outputs.

import pandas as pd
import scipy.stats as st
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')
print(st.ttest_1samp(scores['Exam1'], 82))