import os
import scipy.io as sio
import numpy as np


directory = os.fsencode(r'positive_segments')

maxlist = []
gradMaxList = []



for file in os.listdir(directory):
    filename = os.fsdecode(file)
    os.chdir(r'positive_segments')
    sig = sio.loadmat(filename)
    os.chdir(r'/Users/admin/.spyder-py3')
    sig = sig["d"]
    sig = sig[2, :]
    gradSig = np.gradient(sig)
    maxlist.append(np.amax(sig))
    gradMaxList.append(np.amax(gradSig))
    

    
    
'''
os.chdir(r'positive_segments')
os.chdir(r'/Users/admin/.spyder-py3')
'''