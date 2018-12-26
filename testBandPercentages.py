import os
import scipy.io as sio
import numpy as np
from derivativeTrimmer import trim

directory = os.fsencode(r'positive_segments') #5585 files
i = 0
testSigList = []


for file in os.listdir(directory):
   filename = os.fsdecode(file)
   os.chdir(r'positive_segments')
   sig = sio.loadmat(filename)
   os.chdir(r'/Users/admin/.spyder-py3')
   sig = sig["d"]
   sig = sig[1, :] #2nd channel
   sig = trim(sig, 30)
   if(sig.size == 0):
       continue
   
   testSigList.append(sig)

   
    
   
    
   
   
    

