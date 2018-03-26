# coding:utf-8
from lxml.etree import Element, SubElement, tostring
from xml.dom.minidom import parseString
import glob
import os
import cv2
from tqdm import tqdm  #添加一个进度条显示而已
def txtToXml(image_path, txt_path):
    for txt_file in tqdm(glob.glob(txt_path + '/*.txt')):
        txt_name_ = txt_file.split('/')[-1][:-4]
        data = {"shapes": []}
        im = cv2.imread(image_path + '/' + txt_name_ +'.jpg')
        try:
            im.shape
        except:
            print("bad image")
            continue
        width = im.shape[0]
        height = im.shape[1]
        tree = open(txt_file, 'r', encoding='UTF-8')
        node_root = Element('annotation')
        node_folder = SubElement(node_root, 'folder')
        node_folder.text = 'ICPR'
        node_filename = SubElement(node_root, 'filename')
        node_filename.text = txt_name_+ '.jpg'
        node_size = SubElement(node_root, 'size')
        node_width = SubElement(node_size, 'width')
        node_width.text = str(width)
        node_height = SubElement(node_size, 'height')
        node_height.text = str(height)
        node_depth = SubElement(node_size, 'depth')
        node_depth.text = '3'
        root = tree.readlines()
        for i, line in enumerate(root):
            column = line.split(',')
            node_object = SubElement(node_root, 'object')
            node_name = SubElement(node_object, 'name')
            node_name.text = 'name'    
            node_difficult = SubElement(node_object, 'difficult')
            node_difficult.text = '0'
            node_bndbox = SubElement(node_object, 'bndbox')
            node_xmin = SubElement(node_bndbox, 'x0')
            node_xmin.text = column[0]
            node_ymin = SubElement(node_bndbox, 'y0')
            node_ymin.text = column[1]
            node_xmax = SubElement(node_bndbox, 'x1')
            node_xmax.text = column[2]
            node_ymax = SubElement(node_bndbox, 'y1')
            node_ymax.text = column[3]
            node_xmin = SubElement(node_bndbox, 'x2')
            node_xmin.text = column[4]
            node_ymin = SubElement(node_bndbox, 'y2')
            node_ymin.text = column[5]
            node_xmax = SubElement(node_bndbox, 'x3')
            node_xmax.text = column[6]
            node_ymax = SubElement(node_bndbox, 'y3')
            node_ymax.text = column[7]
        xml = tostring(node_root, pretty_print=True)  #格式化显示，该换行的换行
        dom = parseString(xml)
        # print (xml)
        xmls = os.path.join(os.getcwd(), 'xml', txt_name_)
        #with open(txt_name_ + '.xml', 'w') as f:
        with open(xmls + '.xml', 'w') as f:
            dom.writexml(f, indent='\t', encoding="utf-8")



if __name__ == "__main__":
    data_path = os.path.join(os.getcwd(), 'txt_1000')  #os.getcwd()返回当前所在文件夹
    pic_path = os.path.join(os.getcwd(), 'image_1000')
    txtToXml(pic_path, data_path )
