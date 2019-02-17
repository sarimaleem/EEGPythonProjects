import scipy.io as sio
from featureExtractor import extractPercentages
import matplotlib.pyplot as plt
from derivativeTrimmer import trim
from reconstructBands import denoise
from getBandPercentages import  getSumOfBandsPercentages
import numpy as np

temp = sio.loadmat('positive_segments/c259_00037.mat')["d"][1]
plt.plot(temp)
temp = denoise(temp)
print(extractPercentages(temp))
plt.show()
plt.plot(temp)
plt.show()
plt.plot(np.gradient(temp))
plt.show()




