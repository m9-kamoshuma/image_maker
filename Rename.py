#!/usr/bin/env python
# coding: utf-8

# In[4]:


import cv2
import glob
import os
from natsort import natsorted

def rename(dir_name,new_dir):
    i=0
    images = dir_name + '/' + '*.*'
    files = [i for i in natsorted(glob.glob(images))]
    for file in files:
        img=cv2.imread(file)
        file=str(i)
        cv2.imwrite(os.path.join(new_dir, file+'.jpg'),img)
        i=i+1

