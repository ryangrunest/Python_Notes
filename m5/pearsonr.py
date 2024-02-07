# Python-Function 5.3.1: scipy.stats.pearsonr(x,y).
# The Pearson correlation coefficient function pearsonr(x,y)
# takes in two arrays or DataFrames x and y and outputs the Pearson correlation coefficient and the corresponding two-tailed 
# p-value. The function requires the scipy.stats library.

# The code below uses the Exam1 and Exam4 columns of the ExamScore dataset and outputs the correlation coefficient and the two-tailed 
# p-value obtained.

import pandas as pd
import scipy.stats as st
scores = pd.read_csv("http://data-analytics.zybooks.com/ExamScores.csv")
st.pearsonr(scores['Exam1'],scores['Exam4'])