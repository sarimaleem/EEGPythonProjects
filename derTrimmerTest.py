from derivativeTrimmer import trim
import matplotlib.pyplot as plt
import scipy.io as sio
import numpy as np


testSignal = sio.loadmat('testSegment.mat')
testSignal = testSignal["d"]
testSignal = testSignal[1, :]

plt.plot(testSignal)
plt.plot(np.gradient(testSignal))
plt.cla()


a = trim(testSignal, 25)
plt.plot(a)


