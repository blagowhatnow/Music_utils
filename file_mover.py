#Moves .mp3 files from the directory fma_small/ to done/ for the mp3 
#files for which specgram.py was able to generate spectograms

import os
from pathlib import Path
  
source = 'fma_small/'
destination = 'done/'
  

DIRECTORY = Path("./fma_small")

done_files_png=[]

for fp in DIRECTORY.glob('*.png'): 
     done_files_png.append(str(fp))

done_files_mp3 =[i.replace(".png","") for i in done_files_png]
done_files_mp3=[i.replace("fma_small/","") for i in done_files_mp3]
  
for f in done_files_mp3:
    os.rename( source+f, destination + f)
