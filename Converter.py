import cv2
import numpy as np
import os
import glob
from PIL import Image
from natsort import natsorted

def converter(dir_name,list):
    path = dir_name + '/' + '*.*'
    files = [i for i in natsorted(glob.glob(path))]
    for i in range(len(files)):
        img_s = Image.open(os.path.join(dir_name,files[i]))
        img_s = np.float32(img_s)
        img_s *= 1./255
        Lab0 = cv2.cvtColor(img_s, cv2.COLOR_BGR2Lab)
        L, a, b = cv2.split(Lab0)
        Lab=(L,a,b)
        list.append(Lab)

