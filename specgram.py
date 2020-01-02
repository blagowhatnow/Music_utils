import pylab
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt


fs, frames = wavfile.read("orangek1.wav")

channels = [
    np.array(frames[:, 0]),
    np.array(frames[:, 1])
]

# generate specgram
Pxx, freqs, t, plot = pylab.specgram(
    channels[0],
    NFFT=4096, 
    Fs=44100, 
    detrend=pylab.detrend_none,
    window=pylab.window_hanning,
    noverlap=int(4096 * 0.5))

pylab.axis('off')
pylab.savefig('saveit.png')
pylab.show()
