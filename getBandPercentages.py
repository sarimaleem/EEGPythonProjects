from pywt import WaveletPacket
import numpy as np

def getSumOfBandsPercentages(signal):

    wp = WaveletPacket(data = signal, wavelet = 'db4', maxlevel = 6)
    nodes = [node.path for node in wp.get_level(6, 'natural')]

    delta = np.sum(np.abs(wp[nodes[0]].data))
    theta = np.sum(np.abs(wp[nodes[1]].data))
    alpha = np.sum(np.abs(wp[nodes[2]].data))
    beta = 0
    gamma = 0

    for i in range(3, 9):
        beta += np.sum(np.abs(wp[nodes[i]].data))

    for i in range(9, 14):
        gamma += np.sum(np.abs(wp[nodes[i]].data))
        
    bands = [delta, theta, alpha, beta, gamma]
    sum = np.sum(bands)
    percentages = bands/sum
    percentages *= 100
    return percentages
    



