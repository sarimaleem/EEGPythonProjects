import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

posDelta = np.load("testDeltaPos.npy")
negDelta = np.load("testDeltaNeg.npy")
sns.boxplot(data=[posDelta, negDelta], palette="Set2")

plt.title("Delta Percentages")
plt.xlabel("Candidate Type")
plt.xticks([0, 1], ["Positive", "Negative"])
plt.ylabel("Percentage Span")
plt.show()