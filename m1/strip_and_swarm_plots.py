# loads the necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# loads the titanic dataset
titanic = sns.load_dataset("titanic")

# title
plt.title('Fares paid by passengers of the Titanic by deck', fontsize=20)

# plot
sns.stripplot(x="deck", y="fare", data=titanic);

# saves the image
plt.savefig("titanicstripplot.png")

# shows the image
plt.show()