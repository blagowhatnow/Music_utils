import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from pathlib import Path
from pydub import AudioSegment
from tempfile import NamedTemporaryFile
import librosa

# Directory containing your files
DIRECTORY = Path("./fma_small")

# Configure numpy to ignore divide-by-zero warnings
np.seterr(divide='ignore')

def process_audio_file(fp):
    try:
        # Convert mp3 to wav using pydub
        mp3_audio = AudioSegment.from_file(str(fp), format="mp3")
        with NamedTemporaryFile(suffix='.wav', delete=False) as tmp_wav:
            mp3_audio.export(tmp_wav.name, format="wav")
            FS, data = wavfile.read(tmp_wav.name)

        # If mono channel (1D array)
        if data.ndim == 1:
            plt.specgram(data, Fs=FS, NFFT=128, noverlap=0)
        # If stereo channel (2D array)
        else:
            plt.specgram(data[:, 1], Fs=FS, NFFT=128, noverlap=0)

        # Plot adjustments
        plt.axis('off')
        plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
        plt.margins(0, 0)

        # Save spectrogram image
        plt.savefig(f"{fp.stem}.png")
        plt.cla()  # Clear the current plot to free memory

    except Exception as e:
        print(f"Error processing {fp}: {e}")

# Process all mp3 files in the directory
for mp3_file in DIRECTORY.glob('*.mp3'):
    print(f"Processing {mp3_file}")
    process_audio_file(mp3_file)

