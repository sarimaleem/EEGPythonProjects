import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
from reconstructBands import rec
from getBandPercentages import getSumOfBandsPercentages
from plotSegments import pltWavCoeffs

testSignal = sio.loadmat('testSegment.mat')
testSignal = testSignal["d"]
testSignal = testSignal[1, :]
#testSignal = testSignal[1500:2775]


figure, (ax1, ax2) = plt.subplots(nrows=2)

ax1.plot(testSignal, label = 'original')

gradTest = np.gradient(testSignal)

ax1.plot(gradTest, label = 'original gradient')

recon = rec(testSignal, lowGamma=0)
gradRecon = np.gradient(recon)

ax2.plot(recon, label = 'denoised')
ax2.plot(gradRecon, label = 'denoised gradient')
ax1.legend()
ax2.legend()

pltWavCoeffs(testSignal)

percentages = getSumOfBandsPercentages(recon[480:750])







