import os
import scipy.io as sio
import numpy as np
from derivativeTrimmer import trim
from trimSides import trimSides

posDirectory = os.fsencode(r'positive_segments')  # 5585 files
negDirectory = os.fsdecode(r'negative_segments')  # 32768 files
posPercentages = np.zeros(shape=(5585, 5))
negPercentages = np.zeros(shape=(32768, 5))


posIndex = 0
negIndex = 0
i = 0


# positive segment data
for file in os.listdir(posDirectory):
   filename = os.fsdecode(file)
   os.chdir(r'positive_segments')
   sig = sio.loadmat(filename)
   os.chdir(r'/Users/admin/rpsp')
   sig = sig["d"]
   sig = sig[1]
   sig = trimSides(sig, 2000, 2000)



   i = i+1
   if i%1000 == 0:
      print(i)

for file in os.listdir(negDirectory):
    filename = os.fsdecode(file)
    os.chdir(r'negative_segments')
    sig = sio.loadmat(filename)
    os.chdir(r'/Users/admin/rpsp')
    sig = sig["d"]
    sig = sig[1]
    sig = trimSides(sig, 2000, 2000)






    i = i + 1
    if i % 1000 == 0:
       print(i)


