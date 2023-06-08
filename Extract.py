import os
import cv2
import numpy as np
import PIL.ImageDraw

def extract(dir_name,new_dir):
    files = os.listdir(dir_name)
    for file in files:
        img = PIL.Image.open(os.path.join(dir_name,file))
        small_img = img.resize((10, 10))  # 時間短縮のために解像度を落とす
        color_arr = np.array(small_img)
        w_size, h_size, n_color = color_arr.shape
        color_arr = color_arr.reshape(w_size * h_size, n_color)

        color_mean = np.mean(color_arr, axis=0)
        color_mean = color_mean.astype(int)
        color_mean = tuple(color_mean)
        color_mean=[[[color_mean[0],color_mean[1],color_mean[2]]]]
        color_mean=np.array(color_mean)
        cv2.imwrite(os.path.join(new_dir, file),color_mean)
