#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import cv2

def resize(dir_name, new_dir,h,w):
    files = os.listdir(dir_name)
    for file in files:
        img=cv2.imread(os.path.join(dir_name, file))
        img_resize=cv2.resize(img,(w,h))
        cv2.imwrite(os.path.join(new_dir, file),img_resize)


# %%
