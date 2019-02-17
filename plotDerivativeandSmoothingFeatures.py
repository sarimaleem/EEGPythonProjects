import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.io as sio
from reconstructBands import denoise

sig = sio.loadmat("positive_segments/c259_00001.mat")
sig = sig["d"]
sig = sig[1]
sig = sig[1000:3001]
labels = np.arange(0, np.size(sig), 250)
ticks = labels / 500

plt.plot(sig)
plt.xticks(labels, ticks)
plt.title("Raw Signal")
plt.xlabel("Time (Seconds)")
plt.ylabel("Amplitude (mV)")


plt.figure()
gradSig = np.gradient(sig)
plt.plot(gradSig, color="#cc5200")
plt.xticks(labels, ticks)
plt.title("Raw Signal Gradient")
plt.xlabel("Time (Seconds)")
plt.ylabel("Amplitude (mV)")


plt.figure()
smoothSig = denoise(sig)
plt.plot(smoothSig)
plt.xticks(labels, ticks)
plt.title("Denoised Signal")
plt.xlabel("Time (Seconds)")
plt.ylabel("Amplitude (mV)")


plt.figure()
gradSmoothSig = np.gradient(smoothSig)
plt.plot(gradSmoothSig, color="#cc5200")
plt.xticks(labels, ticks)
plt.title("Denoised Signal Gradient")
plt.xlabel("Time (Seconds)")
plt.ylabel("Amplitude (mV)")


plt.show()
