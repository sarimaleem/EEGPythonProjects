import os
import scipy.io as sio
import time
from featureExtractor import extract

posDirectory = os.fsencode(r'positives_test')  # 21844 files
negDirectory = os.fsdecode(r'negatives_test')  # 32766 files

totalPosFiles = 21844
totalNegFiles = 32766

truePos = 0
falsePos = 0


posIndex = 0
negIndex = 0
i = 0


time1 = time.time()

# positive segment data
for file in os.listdir(posDirectory):

    posIndex += 1

    filename = os.fsdecode(file)
    os.chdir(posDirectory)
    sig = sio.loadmat(filename)
    os.chdir(r'/Users/admin/rpsp')
    sig = sig["d"]
    sig = sig[1]

    truePos += extract(sig)



    i = i + 1
    if i % 1000 == 0:
        print(i)

for file in os.listdir(negDirectory):


    negIndex += 1


    filename = os.fsdecode(file)
    os.chdir(negDirectory)
    sig = sio.loadmat(filename)
    os.chdir(r'/Users/admin/rpsp')
    sig = sig["d"]
    sig = sig[1]

    falsePos += extract(sig)

    i = i + 1
    if i % 1000 == 0:
        print(i)


time2 = time.time()

totalTime = time2 - time1

print(truePos/totalPosFiles)
print((totalNegFiles-falsePos)/totalNegFiles)