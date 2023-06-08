#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import cv2
import os

def main_resize(main_path,new_dir,num_w,num_h):
    img=cv2.imread(main_path)
    main_h,main_w=img.shape[:2]
    dh_=main_h-(main_h//num_h)*num_h
    dh = (main_h//num_h)*(num_h+1)-main_h
    dw_=main_w-(main_w//num_w)*num_w
    dw = (main_w//num_w)*(num_w+1)-main_w
    if dh_<=dh:
        main_h=(main_h//num_h)*num_h
    else:
        main_h=(main_h//num_h)*(num_h+1)
    if dw_<=dw:
        main_w=(main_w//num_w)*num_w
    else:
        main_w=(main_w//num_w)*(num_w+1)

    img_resize = cv2.resize(img,(main_w,main_h))
    cv2.imwrite(os.path.join(new_dir,os.path.basename(main_path)),img_resize)


# %%
