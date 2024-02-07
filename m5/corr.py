# zyDE 5.3.1: corr().
# The correlation function DataFrame.corr() calculates the pairwise correlation of the columns in the dataframe and outputs a correlation matrix.

# The code below uses the Exam1 and Exam2 columns of the ExamScore dataset and produces a 
#  2x2 correlation matrix.

# The code below uses the Exam1, Exam2, Exam3, and Exam4 columns of the ExamScore dataset and produces a 
#  4x4 correlation matrix.

import pandas as pd
scores = pd.read_csv("ExamScores.csv")
print(scores[['Exam1','Exam2']].corr())
print(scores[['Exam1','Exam2','Exam3','Exam4']].corr())