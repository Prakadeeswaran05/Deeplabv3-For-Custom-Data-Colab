import tensorflow as tf
from PIL import Image
from tqdm import tqdm
import numpy as np
import cv2

import os, shutil

# palette (color map) describes the (R, G, B): Label pair
palette = {(64,  128,  64): 0,
           (192,  0,  128): 1,	
           (0,  128,  192): 2,	
           (0,  128,  64): 3,	
           (128,  0,  0	): 4,	
           (64,  0,  128): 5,	
           (64,  0,   192): 6,	
           (192,  128,  64): 7,	
           (192,  192,  128): 8,	
           (64,  64,  128): 9,	
           (128,  0,  192): 10,	
           (192,  0,  64): 11,	
           (128,  128,  64): 12,	
           (192,  0,  192): 13,	
           (128,  64,  64): 14,	
           (64,  192,  128): 15,	
           (64,  64,  0): 16,
           (128,  64,  128): 17,	
           (128,  128,  192): 18,	
           (0,  0,  192): 19,		
           (192,  128,  128): 20,	
           (128,  128,  128): 21,	
           (64,  128,  192): 22, 
           (0,  0,  64): 23,		
           (0,  64,  64): 24,		
           (192,  64,  128): 25,	
           (128,  128,  0): 26,	
           (192,  128,  192): 27,	
           (64,  0,  64): 28,		
           (192,  192,  0): 29,	
           (0,  0,  0): 30,		
           (64,  192,  0): 31
           }
def convert_from_color_segmentation(arr_3d):
    arr_2d = np.zeros((arr_3d.shape[0], arr_3d.shape[1]), dtype=np.uint8)

    for c, i in palette.items():
        m = np.all(arr_3d == np.array(c).reshape(1, 1, 3), axis=2)
        arr_2d[m] = i
    return arr_2d


label_dir = 'C:\\Users\\kesav\\Downloads\\PQR\\dataset\\SegmentationClass\\'
new_label_dir = 'C:\\Users\\kesav\\Downloads\\PQR\\dataset\\SegmentationClassRaw\\'

if not os.path.isdir(new_label_dir):
	print("creating folder: ",new_label_dir)
	os.mkdir(new_label_dir)
else:
	print("Folder alread exists. Delete the folder and re-run the code!!!")


label_files = os.listdir(label_dir)

for l_f in tqdm(label_files):
    img=Image.open(label_dir + l_f)
    
    arr = np.array(Image.open(label_dir + l_f))
    arr = arr[:,:,0:3]
    arr_2d = convert_from_color_segmentation(arr)
    
   
    Image.fromarray(arr_2d).save(new_label_dir + l_f)
