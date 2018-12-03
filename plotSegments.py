import matplotlib.pyplot as plt
from pywt import wavedec

def pltWavCoeffs(signal):
    
    coeffs = wavedec(signal, 'db4', level=6, axis=0)
    cA6, cD6, cD5, cD4, cD3, cD2, cD1 = coeffs
    
    figure, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(nrows=6)
    
    ax1.plot(cA6)
    ax1.set_title('cA6')
    
    ax2.plot(cD6)
    ax2.set_title('cD6')
    
    ax3.plot(cD5)
    ax3.set_title('cD5')
    
    ax4.plot(cD4)
    ax4.set_title('cD4')
    
    ax5.plot(cD3)
    ax5.set_title('cD3')
    
    ax6.plot(cD2)
    ax6.set_title('cD2')

