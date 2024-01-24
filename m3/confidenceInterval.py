import scipy.stats as stats
import pandas as pd

scores = [71, 73, 69, 65, 70, 75, 75]
scores_data_frame = pd.DataFrame(scores, columns=['scores'])

sigma = 2.5
mean = scores_data_frame.mean()
print('mean', mean)

standard_deviation = scores_data_frame['scores'].std()

# The standard error is standard deviation/sqrt(number of samples)
stderr = standard_deviation/(len(scores) ** 0.5)

print(stats.norm.interval(0.99, mean, stderr))
