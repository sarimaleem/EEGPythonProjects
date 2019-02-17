from plotSegments import pltWavCoeffs
import numpy as np
import scipy.io as sio
import seaborn as sns


sig = sio.loadmat("positives_test/CW0108_P224_00002.mat")
sig = sig["d"][1]

pltWavCoeffs(sig)

