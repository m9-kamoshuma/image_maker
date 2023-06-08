import os
import shutil

def dirmkr(name,crdir):
    dir_name=os.path.join(crdir,name)
    if  os.path.exists(dir_name):
        shutil.rmtree(dir_name)
    os.mkdir(dir_name)

