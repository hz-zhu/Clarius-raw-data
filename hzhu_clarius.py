import shutil
import os
import subprocess

from hzhu_gen import *

import numpy as np
from scipy.signal import hilbert
import matplotlib.pyplot as plt
import sys
import rdataread as rd

class CData:
    
    def __init__(self, folder_path, filename, lzop_path):
        self.folder_path = folder_path
        self.filename = filename
        self.lzop_path = lzop_path
        
        self.folder_name = os.path.join(self.folder_path, *filename.split('.')[0:-1])
        shutil.unpack_archive(os.path.join(self.folder_path, filename), self.folder_name)
        
        self.files = ls_file(self.folder_name)
        
        for item in self.files:
            if '.raw.lzo' in item:
                out = subprocess.run('\"%s\\unzip_data.exe\" -d \"%s\"'%(self.lzop_path, os.path.join(self.folder_name, item)), shell = True)
                os.remove(os.path.join(self.folder_name, item))
        
        self.files = ls_file(self.folder_name)
    
    def get_rf(self):
        for item in self.files:
            if 'rf.raw' in item:
                return rd.read_rf(os.path.join(self.folder_name, item))
        return None
    
    def plot_rf(self, start=0, stop=float('inf'), step=1):
        hdr, timestamps, data = self.get_rf()
        stop = min(hdr['frames'], stop)
    
        # covnert to B 
        bdata = np.zeros((hdr['lines'], hdr['samples'], hdr['frames']), dtype='float')
        for frame in range(start, stop, step):
            bdata[:,:,frame] = 20 * np.log10( np.abs(1 + hilbert(data[:,:,frame])) )

        # display images
        for frame in range(start, stop, step):
            plt.figure(figsize=(10,5))
            plt.subplot(1,2,1)
            plt.imshow(np.transpose(data[:,:,frame]), cmap=plt.cm.plasma, aspect='auto', vmin=-1000, vmax=1000 )
            plt.title('RF frame ' + str(frame))
            plt.subplot(1,2,2)
            plt.imshow(np.transpose(bdata[:,:,frame]), cmap=plt.cm.gray, aspect='auto', vmin=15, vmax=70 )
            plt.title('sample B frame ' + str(frame))
            plt.show()    