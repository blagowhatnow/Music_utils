import os
import pylab
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import glob

path=""

for filename in glob.glob(os.path.join(path, '*.wav')):
    fs, frames = wavfile.read(filename)

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

    plt.axis('off')
    plt.savefig(filename.replace('.wav','')+".png")
    plt.close()
