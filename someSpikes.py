import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
import seaborn as sns

sig = sio.loadmat("positives_test/CW0108_P224_00002.mat")

sig = sig["d"][1]
sig = sig[0:1600]

sns.lineplot(data=sig)
sns.set_style("ticks")


labels = np.arange(0, np.size(sig), 250)
ticks = labels / 500
plt.xticks(labels, ticks)
plt.xlabel("Time (Seconds)")
plt.title("Repetitive Spike")
plt.ylabel("Amplitude (mV)")

plt.show()
