# The st.ttest_rel(x, y) function takes two arrays or DataFrame columns x and y with the same length as inputs and returns the 
# t-statistic and the corresponding two-tailed 
# p-value as outputs.
# The code below loads the exam scores data and uses a paired 
# t-test for the hypotheses.

import scipy.stats as st
import pandas as pd
df = pd.read_csv('ExamScores.csv')
print(st.ttest_rel(df['Exam1'],df['Exam2']))


# The st.ttest_ind(x, y) command takes two arrays or DataFrame columns x and y as inputs and returns the 
# t-statistic and the corresponding two-tailed 
# p-value as outputs.
# The code below conducts the test for the packing machine example above. Both the two-tailed test and the one-tailed test are conducted.

import scipy.stats as st
import pandas as pd
df = pd.read_csv('Machine.csv')

# Two-tailed test
print(st.ttest_ind(df['Old'],df['New'],equal_var=False, alternative="two-sided"))

# One-tailed test
print(st.ttest_ind(df['Old'],df['New'],equal_var=False, alternative="greater"))