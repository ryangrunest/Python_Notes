# loads the necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# loads the ExamScores dataset
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')

# transforms the data
df = pd.melt(scores, value_name = "Score", var_name = "Exam")

# plot
sns.boxplot(x="Exam", y="Score", data=df);

# saves the image
plt.savefig("Examsboxplots.png")

# shows the image
plt.show()