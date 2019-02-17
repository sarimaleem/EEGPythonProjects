import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
import seaborn as sns

sig = sio.loadmat("negatives_test/280_00002.mat")

sig = sig["d"][1]
sig = sig[1500:3100]

sns.lineplot(data=sig)
sns.set_style("ticks")


labels = np.arange(0, np.size(sig), 250)
ticks = labels / 500
plt.xticks(labels, ticks)
plt.xlabel("Time (Seconds)")
plt.title("Sleep Signal")
plt.ylabel("Amplitude (mV)")

plt.show()