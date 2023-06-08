import os
from PIL import Image

def concat(dir_name,list,num_w,num_h,goal_dir,name):
    k=0
    img = Image.open(os.path.join(dir_name,'0.jpg'))
    w, h = img.size
    canvas = Image.new("RGBA", (w * num_w, h * num_h))

    for i in range(len(list)):
        img = Image.open(os.path.join(dir_name,str(list[i])+'.jpg'))
        w, h = img.size
        j = i % num_w  
        canvas.paste(img, (w * j, h * k))
        if i !=0 and (i+1) % num_w==0:
            k=k+1  

    #画像出力、保存
    canvas.show()
    canvas.save(goal_dir+'/'+name+'.png')
