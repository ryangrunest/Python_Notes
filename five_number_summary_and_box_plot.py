import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# reads the mtcars.csv file into a dataframe called mtcars
mtcars = pd.read_csv("https://data-analytics.zybooks.com/mtcars.csv")

# prints the first few lines of mtcars
print(mtcars.head())

# 5 number summary
print(mtcars.wt.describe())

# box plot
sns.boxplot(mtcars.wt, width=0.35)

# saves the image
plt.savefig("boxplot.png")

# shows the image
plt.show()