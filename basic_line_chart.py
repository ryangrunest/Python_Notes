# The code below loads a dataset containing unemployment rates in the United States from 1980 to 2017 and plots the data as a line chart.
# imports the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# loads the unemployment dataset
unemployment = pd.read_csv('./unemployment.csv')

# title
plt.title('U.S. unemployment rate', fontsize = 20)

# x and y axis labels
plt.xlabel('Year')
plt.ylabel('% of total labor force')

# plot
plt.plot(unemployment["Year"], unemployment["Value"])

# saves the image
plt.savefig("unemployment.png")

# shows the image
plt.show()


