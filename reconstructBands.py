from pywt import wavedec
from pywt import waverec
import numpy as np


test = sio.loadmat('testSegment.mat')
test = test["d"]
test = test[1, :]

def rec(signal, delta = 1, theta = 1, alpha = 1, beta = 1, lowGamma = 1, midGamma = 0, highGamma = 0):
    coeffs = wavedec(signal, 'db4', level=6, axis=0)
    cA6, cD6, cD5, cD4, cD3, cD2, cD1 = coeffs
    
    cA6 = cA6 * delta 
    cD6 = cD6 * theta
    cD5 = cD5 * alpha
    cD4 = cD4 * beta
    cD3 = cD3 * lowGamma
    cD2 = cD2 * midGamma
    cD1 = cD1 * highGamma
    
    newCoeffs = [cA6, cD6, cD5, cD4, cD3, cD2, cD1]
    reconstructed = waverec(newCoeffs, 'db4')
    return reconstructed

test2 = rec(test, lowGamma = 0)