import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

train = np.load("train3.npy")
posDelta = train[0:5585, 0]
negDelta = train[5585:, 0]

positive_size = np.size(posDelta)
negative_size = np.size(negDelta)

TPR = []
FPR = []
x = np.arange(0, 1, 0.01)
y = np.arange(0, 1, 0.01)


for i in range(1000):
    j = i/10

    falseNegatives = np.sum(posDelta > j)
    truePositives = positive_size - falseNegatives
    truePositiveRate = truePositives/positive_size

    trueNegatives = np.sum(negDelta > j)
    falsePositives = negative_size - trueNegatives
    falsePositiveRate = falsePositives/negative_size

    TPR.append(truePositiveRate)
    FPR.append(falsePositiveRate)

    if j ==60:
        print("60")
        print(falsePositiveRate)
        print(truePositiveRate)
        print()


    if j == 50:
        print("50")
        print(falsePositiveRate)
        print(truePositiveRate)
        print()


    if j == 40:
        print("40")
        print(falsePositiveRate)
        print(truePositiveRate)
        print()





sns.set_style("whitegrid")
sns.lineplot(FPR, TPR, palette="Set2")
plt.plot(x, y, linestyle="-.", color="red", label = "Random Guess")
plt.title("Receiver Operating Characteristic")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.annotate('Thresh=60', xy=(0.8029170353644769,0.9974932855863922), xytext=(0.8029170353644769,0.9374932855863922))
plt.plot(0.8029170353644769,0.9974932855863922, 'ko')

plt.annotate('Thresh=40', xy=(0.55789826991731,0.9606087735004476), xytext=(0.49789826991731,0.9006087735004476))
plt.plot(0.55789826991731,0.9606087735004476, 'ko')

plt.annotate('Thresh=50', xy=(0.7194641930857718,0.9928379588182632), xytext=(0.6294641930857718,0.9328379588182632))
plt.plot(0.7194641930857718,0.9928379588182632, 'ko')

plt.show()
