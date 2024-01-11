# loads the necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# loads the titanic dataset
titanic = sns.load_dataset("titanic")

# title
plt.title('Fares paid by passengers of the Titanic by deck', fontsize=20)

# plot
sns.swarmplot(x="deck", y="fare", hue = "sex", data=titanic);

# saves the image
plt.savefig("titanicswarmplot.png")

# shows the image
plt.show()