import os
import scipy.io as sio
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.utils import shuffle
from featureExtractor import extractPercentages
from trimSides import trimSides




j = 0

testPercentages = np.zeros(shape=(54611, 5))
testPercentageLabels = np.ones(shape=(54611))


pos = np.zeros(shape=(21844, 5))
neg = np.zeros(shape=(32767, 5))


testPercentageLabels[21844:] = 0


#38353 files total


posDirectory = os.fsencode(r'positive_segments')  # 5585 files
negDirectory = os.fsdecode(r'negative_segments')  # 32768 files
testPosDirectory = os.fsencode(r'positives_test') # 21844 files
testNegDirectory = os.fsencode(r'negatives_test') # 32767 files

i = 0


for file in os.listdir(testPosDirectory):

    filename = os.fsdecode(file)
    os.chdir(testPosDirectory)
    sig = sio.loadmat(filename)
    os.chdir(r'/Users/admin/rpsp')
    sig = sig["d"]
    sig = sig[1]

    p = extractPercentages(sig)

    pos[j] = p

    i = i + 1
    j = j + 1


    if i%1000 == 0:
        print(i)

k = 0
for file in os.listdir(testNegDirectory):

    filename = os.fsdecode(file)
    os.chdir(testNegDirectory)
    sig = sio.loadmat(filename)
    os.chdir(r'/Users/admin/rpsp')
    sig = sig["d"]
    sig = sig[1]

    sig = trimSides(sig, 2000, 2000)
    p = extractPercentages(sig)
    neg[k] = p


    i = i+1
    k = k+1

    if i%1000 == 0:
        print(i)




deltaPos = pos[:, 0]
deltaNeg = neg[:, 0]






#model = RandomForestClassifier()
#model.fit(train, labels)



