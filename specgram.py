import os
from pydub import AudioSegment
import matplotlib.pyplot as plt
from scipy.io import wavfile
from tempfile import mktemp
from pathlib import Path

# assign directory
DIRECTORY = Path("./fma_small")

import glob

# ...
for fp in DIRECTORY.glob('*.mp3'):
     print(fp)
     mp3_audio = AudioSegment.from_file(str(fp), format="mp3")  # read mp3
     wname = mktemp('.wav')  # use temporary file
     mp3_audio.export(wname, format="wav")  # convert to wav
     FS, data = wavfile.read(wname)  # read wav file
     if data.ndim==1 :
        plt.specgram(data, Fs=FS, NFFT=128, noverlap=0)
        plt.axis('off')
        plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
        plt.margins(0,0)
        plt.savefig(str(fp)+".png")
     else:
        plt.specgram(data[:,1], Fs=FS, NFFT=128, noverlap=0)
        plt.axis('off')
        plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
        plt.margins(0,0)
        plt.savefig(str(fp)+".png")

   
