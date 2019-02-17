import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

train = np.load("train3.npy")
posDelta = train[0:5585, 0]
negDelta = train[5585:, 0]
sns.boxplot(data=[posDelta, negDelta], palette="Set2")

plt.title("Delta Percentages")
plt.xlabel("Candidate Type")
plt.xticks([0, 1], ["Positive", "Negative"])
plt.ylabel("Percentage Span")
plt.show()

