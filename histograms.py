import pandas as pd
import matplotlib.pyplot as plt
heights = pd.read_csv('http://data-analytics.zybooks.com/height.csv')

fig, ax = plt.subplots()
plt.hist(heights['Height'], bins=6)
ax.set_xlabel('Height')
ax.set_ylabel('Frequency')
plt.savefig('histogram6.png')
plt.show()