# loads the necessary modules
import matplotlib.pyplot as plt
import seaborn as sns

# loads the iris data set
df = sns.load_dataset("iris")

# title
plt.title('Petal length and width of iris', fontsize=20)

# plot
sns.regplot(df["petal_length"], df["petal_width"], ci=None, fit_reg=False);

# saves the image
plt.savefig("irisscatterplot.png")

# shows the image
plt.show()