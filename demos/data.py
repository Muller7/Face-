
#coding=utf-8
import os
import json


path = os.path.abspath('.')
p_path =os.path.join(path,'info')
image_list = os.listdir(p_path)

stu_id_list=[]
for name in image_list:
    name2 = str(name.split('.')[0])
    stu_id_list.append(name2)

print stu_id_list



