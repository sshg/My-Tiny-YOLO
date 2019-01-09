# -*- coding: UTF-8 -*-
#此脚本修改自voc_label.py。修改的原因是：我的训练集跟voc有些不同。
#由于数据集中包括用于训练的数据和用于验证的数据，所以此脚本可能需要分别对这两种数据各运行一次，对两种数据只需要简单地注释掉相应语句即可
#这个脚本需要train.txt ，这个文件是我用脚本creat_list.py生成的，保存了用于训练的图片的名字id,保存了用于训练的图片的名字
#这个脚本需要val.txt文件，这个文件是我用脚本creat_list.py生成的，保存了用于验证的图片的名字id,保存了用于验证的图片的名字
#这个脚本还需要xml格式的标签文件，我的训练集xml文件的格式与voc2007的类似，xml文件的名称与对应的用于训练的图片的名称相同
#这个脚本会生成 indrared_train.txt文件 ，用于保存每一用于训练的图片的完整的路径，随后会被voc.data yolo.c使用
#这个脚本会生成 indrared_val.txt文件 ，用于保存每一用于验证的图片的完整的路径，随后会被voc.data yolo.c使用
#这个脚本还会生成 txt格式的yolo可识别的标签文件，转换自每一个用于训练或验证的图片对应的xml文件，txt格式的文件名称与对应的xml文件名相同，但是内容不同，扩展名不同
#这个脚本 需要与图片对应的xml文件所在的地址，需要，转换后生成的txt的完整保存路径
import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
#sets=[('2012', 'train'), ('2012', 'val'), ('2007', 'train'), ('2007', 'val'), ('2007', 'test')] #按照自己的文件格式改的，不需要判断是那个voc数据包
classes = ["111"]#因为我的数据集只有一个类别
def convert(size, box):#voc_label.py 自带的函数，没有修改
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
def convert_annotation(image_id):
    #in_file = open('VOCdevkit/VOC%s/Annotations/%s.xml'%(year, image_id))
    in_file = open('/home/shgao/boat/annotations/%s.xml'%(image_id)) #与图片对应的xml文件所在的地址
    out_file = open('/home/shgao/darknet_mobilenet/my_scripts/VOCtrainset/%s.txt'%(image_id),'w') #与此xml对应的转换后的txt，这个txt的保存完整路径
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')  #访问size标签的数据
    w = int(size.find('width').text)#读取size标签中宽度的数据
    h = int(size.find('height').text)#读取size标签中高度的数据

    for obj in root.iter('object'):
       # difficult = obj.find('difficult').text   #由于自己的文件里面没有diffcult这一个标签，所以就屏蔽之
        cls = obj.find('name').text
        if cls not in classes :#or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')   #访问boundbox标签的数据并进行处理，都按yolo自带的代码来，没有改动
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

if __name__ == '__main__':
#image_ids = open('VOCdevkit/VOC%s/ImageSets/Main/%s.txt'%(year, image_set)).read().strip().split()  #之前代码是按照sets里面的字符来访问保存有图片名字的train或者val的txt文件
    image_ids = open('/home/shgao/darknet_mobilenet/my_scripts/train.txt').read().strip().split()  #如果是训练集数据打开这一行，注释下一行
#image_ids = open('/home/yolo_v2_tinydarknet/darknet/infrared/val.txt').read().strip().split()  #如果是验证数据集数据打开这一行，注释上一行
#list_file = open('%s_%s.txt'%(year, image_set), 'w')
    list_file = open('infrared_val.txt', 'w')     #把结果写入到indrared_train.txt文件中，如果是训练集数据打开这一行，注释下一行
#list_file = open('infrared_val.txt', 'w')     #把结果写入到indrared_train.txt文件中，如果是验证数据集数据打开这一行，注释上一行
    for image_id in image_ids:
        #list_file.write('%s/VOCdevkit/VOC%s/JPEGImages/%s.jpg\n'%(wd, year, image_id))
        list_file.write('/home/shgao/boat/images/%s.jpg\n'%(image_id))  #把每一用于训练或验证的图片的完整的路径写入到infrared_train.txt中  这个文件会被voc.data yolo.c调用
        convert_annotation(image_id)   #把图片的名称id传给函数，用于把此图片对应的xml中的数据转换成yolo要求的txt格式
    list_file.close() #关闭文件
