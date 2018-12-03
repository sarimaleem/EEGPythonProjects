import numpy as np
from reconstructBands import denoise

def trim(sig, threshold):
    
    smoothSig = denoise(sig) #denoised signal
    derSig = np.gradient(smoothSig) #derivative of denoised signal 
    
    if(np.where(derSig > threshold) == []): #if there is no value in the array that meets the threshold return an empty array
        return np.array([])
    
    first = np.argmax(derSig > threshold) #first index where signal is above thershold
    last = derSig.size - np.argmax(np.flip(derSig, 0) > threshold)
    
    print(first)
    print(last)
    
    return smoothSig[first:last]

    
    
