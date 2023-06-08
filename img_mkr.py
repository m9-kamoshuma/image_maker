#!/usr/bin/env python
# coding: utf-8

# In[3]:

import os
import PySimpleGUI as sg

###### 画像選択、保存先 #######
dir_img = sg.popup_get_folder('画像が入ったフォルダを指定してください')
goal_dir = sg.popup_get_folder('画像の保存先フォルダを指定してください')
main_path = sg.popup_get_file('メイン画像を指定してください')


#保存する名前,パラメータ設定
import result_name
list=[0]*5
list[0],list[1],list[2],list[3],list[4],=result_name.name()
name=list[0]
unit_h=int(list[1])
unit_w=int(list[2])
num_h=int(list[3])
num_w=int(list[4])

#temp
crdir=os.getcwd()
import make_dir
make_dir.dirmkr('rename',crdir)
make_dir.dirmkr('resize',crdir)
make_dir.dirmkr('img_unit',crdir)
make_dir.dirmkr('resize_main',crdir)
make_dir.dirmkr('sepa',crdir)
make_dir.dirmkr('sepa_unit',crdir)


dir_for_rename=os.path.join(crdir,'rename')
dir_for_resize=os.path.join(crdir,'resize')
dir_for_unit=os.path.join(crdir,'img_unit')
dir_for_resize_main=os.path.join(crdir,'resize_main')
dir_for_sepa=os.path.join(crdir,'sepa')
dir_for_sepaunit=os.path.join(crdir,'sepa_unit')

#########操作用に写真名を変換#######

import Rename
Rename.rename(dir_img,dir_for_rename)

#########画像サイズ変換（写真結合用）############
import Resize
import Extract
Resize.resize(dir_for_rename,dir_for_resize,unit_h,unit_w)
Extract.extract(dir_for_rename,dir_for_unit)

#メイン画像のサイズ変換（指定した数字でわれるようにするため）
import Main_resize
Main_resize.main_resize(main_path,dir_for_resize_main,num_w,num_h)

##########メイン写真分割&色抽出##########
from Split import split
split(os.path.join(dir_for_resize_main,os.path.basename(main_path)),dir_for_sepa,num_w,num_h)
Extract.extract(dir_for_sepa,dir_for_sepaunit)

##########RGB2Lab##########
list_for_unit=[]
list_for_sepa=[]
from Converter import converter
converter(dir_for_unit,list_for_unit)
converter(dir_for_sepaunit,list_for_sepa)

##########判定&結合##########
from PrintNum import printNum
Numlist=printNum(list_for_sepa,list_for_unit)


from Concat import concat
concat(dir_for_resize,Numlist,num_w,num_h,goal_dir,name)

from End import end
end()

# In[ ]:




