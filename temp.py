import os
import scipy.io as sio
import numpy as np
from reconstructBands import denoise


directory = os.fsencode(r'positive_segments') #5585 files
gradMaxList = np.zeros(shape=(5585,3))
sigList = []
lowVals = [] #all values with max gradient below 20

i = 0
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    os.chdir(r'positive_segments')
    sig = sio.loadmat(filename)
    os.chdir(r'/Users/admin/.spyder-py3')
    sig = sig["d"]
    sigList.append(sig)
    sig = sig[0, :]
    denoisedSig = denoise(sig)
    gradSig = np.gradient(denoisedSig)
    gradSig.sort()
    gradSig = np.abs(gradSig)
    threeHighestValues = gradSig[-3:]
    gradMaxList[i] = threeHighestValues # highest three values are appended
    if threeHighestValues[2] < 20:
        lowVals.append(i)
    i = i+1
    
    




    
    
    

