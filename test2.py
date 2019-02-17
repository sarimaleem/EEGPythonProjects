import os
import scipy.io as sio
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.utils import shuffle
from featureExtractor import extractPercentages

train = np.zeros(shape=(38358, 5))
labels = np.ones(shape=(38358))
labels[5585:] = 0



j = 0

testPercentages = np.zeros(shape=(54611, 5))
testPercentageLabels = np.ones(shape=(54611))

testPercentageLabels[21844:] = 0

#38353 files total


posDirectory = os.fsencode(r'positive_segments')  # 5585 files
negDirectory = os.fsdecode(r'negative_segments')  # 32768 files
testPosDirectory = os.fsencode(r'positives_test')
testNegDirectory = os.fsencode(r'negatives_test')

i = 0
'''
for file in os.listdir(posDirectory):

    filename = os.fsdecode(file)
    os.chdir(r'positive_segments')
    sig = sio.loadmat(filename)
    os.chdir(r'/Users/admin/rpsp')
    sig = sig["d"]
    sig = sig[1]

    train[i] = extractPercentages(sig)
    i = i+1
    if i % 1000 == 0:
        print(i)


for file in os.listdir(negDirectory):

    filename = os.fsdecode(file)
    os.chdir(r'negative_segments')
    sig = sio.loadmat(filename)
    os.chdir(r'/Users/admin/rpsp')
    sig = sig["d"]
    sig = sig[1]

    train[i] = extractPercentages(sig)
    i = i+1
    if i % 1000 == 0:
        print(i)

'''


for file in os.listdir(testPosDirectory):

    filename = os.fsdecode(file)
    os.chdir(testPosDirectory)
    sig = sio.loadmat(filename)
    os.chdir(r'/Users/admin/rpsp')
    sig = sig["d"]
    sig = sig[1]

    testPercentages[j] = extractPercentages(sig)

    i = i+1
    j = j+1

    if i%1000 == 0:
        print(i)

for file in os.listdir(testNegDirectory):

    filename = os.fsdecode(file)
    os.chdir(testNegDirectory)
    sig = sio.loadmat(filename)
    os.chdir(r'/Users/admin/rpsp')
    sig = sig["d"]
    sig = sig[1]

    testPercentages[j] = extractPercentages(sig)

    i = i+1
    j = j+1
    if i%1000 == 0:
        print(i)




#model = RandomForestClassifier()
#model.fit(train, labels)



