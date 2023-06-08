#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import os

def split(main_path,new_dir,num_w,num_h):
    #画像の読み込み
    img=cv2.imread(main_path)
    h,w=img.shape[:2]

    #画像の分割処理
    cx=0
    cy=0
    k=0
    for j in range(num_h):
        for i in range(num_w):
            split_img=img[cy:cy+int(h/num_h),cx:cx+int(w/num_w),:]
            cv2.imwrite(os.path.join(new_dir,str(k)+'.jpg'),split_img)
            cx=cx+int(w/num_w)
            k=k+1
        cx=0
        cy=cy+int(h/num_h)

