import os
import scipy.io as sio
import numpy as np
from derivativeTrimmer import trim
from trimSides import trimSides
from getBandPercentages import getSumOfBandsPercentages
import time


posDirectory = os.fsencode(r'positive_segments')  # 5585 files
negDirectory = os.fsdecode(r'negative_segments')  # 32768 files
posPercentages = np.zeros(shape=(5585, 5))
negPercentages = np.zeros(shape=(32768, 5))

posIndex = 0
negIndex = 0
zeroOrOneSizes = 0
i = 0

trimTime = 0
wavTime = 0
otherStuffTime = 0


# positive segment data
for file in os.listdir(posDirectory):

    time1 = time.time()
    filename = os.fsdecode(file)
    os.chdir(r'positive_segments')
    sig = sio.loadmat(filename)
    os.chdir(r'/Users/admin/rpsp')
    sig = sig["d"]
    sig = sig[1]
    time2 = time.time()
    otherStuffTime += time2 - time1


    time1 = time.time()
    #sig = trimSides(sig, 2000, 2000)
    sig = trim(sig, 20)
    time2 = time.time()
    trimTime += time2 - time1


    time1 = time.time()
    if sig.size < 2:
        zeroOrOneSizes += 1

    percentages = getSumOfBandsPercentages(sig)
    posPercentages[i] = percentages
    time2 = time.time()
    wavTime += time2 - time1

    i = i + 1
    if i % 1000 == 0:
        print(i)

for file in os.listdir(negDirectory):

    time1 = time.time()
    filename = os.fsdecode(file)
    os.chdir(r'negative_segments')
    sig = sio.loadmat(filename)
    os.chdir(r'/Users/admin/rpsp')
    sig = sig["d"]
    sig = sig[1]
    time2 = time.time()
    otherStuffTime += time2 - time1

    time1 = time.time()
    #sig = trimSides(sig, 2000, 2000)
    sig = trim(sig, 20)
    time2 = time.time()
    trimTime += time2 - time1

    time1 = time.time()
    if sig.size < 2:
        zeroOrOneSizes += 1

    percentages = getSumOfBandsPercentages(sig)
    negPercentages[i - 5585] = percentages

    if(percentages[0] > 75):
        print(filename)


    time2 = time.time()
    wavTime += time2-time1

    i = i + 1
    if i % 1000 == 0:
        print(i)

