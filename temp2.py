import os
import scipy.io as sio
import numpy as np
from reconstructBands import denoise

def maxArr(arr1, arr2, arr3):
    max1 = np.amax(arr1)
    max2 = np.amax(arr2)
    max3 = np.amax(arr3)
    if max1 > max2 and max1 > max3:
        return arr1
    elif max2 > max3:
        return arr2
    return arr3

directory = os.fsencode(r'positive_segments') #5585 files
gradMaxList = np.zeros(shape=(5585,3))
sigList = []
lowVals = [] #all values with max gradient below 20

i = 0

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    os.chdir(r'positive_segments')
    sig = sio.loadmat(filename)
    os.chdir(r'/Users/admin/rpsp')
    sig = sig["d"]
    sigList.append(sig)
    
    chan1sig = denoise(sig[0, :])
    chan2sig = denoise(sig[1, :])
    chan3sig = denoise(sig[2, :])
    
    chan1gradient = np.abs(np.gradient(chan1sig))
    chan2gradient = np.abs(np.gradient(chan2sig))
    chan3gradient = np.abs(np.gradient(chan3sig))
    
    chan1maxlist = np.sort(chan1gradient)[-3:]
    chan2maxlist = np.sort(chan2gradient)[-3:]
    chan3maxlist = np.sort(chan3gradient)[-3:]
    
    threeHighestValues = maxArr(chan1maxlist, chan2maxlist, chan3maxlist) 

    gradMaxList[i] = threeHighestValues # highest three values are appended
    if threeHighestValues[2] < 20:
        lowVals.append(i)
    i = i+1
    

