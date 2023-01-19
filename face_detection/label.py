import os
import cv2
import math
import shutil

import numpy as np
import matplotlib.pyplot as plt

from typing import Union

faces_dir = './face-dataset'
dest_dir = 'final-dataset'

names = {}

## To load an image and create np array of that image
def load_image(image: Union[str, np.ndarray]) -> np.ndarray:
    # Image provided ad string, loading from file ..
    if isinstance(image, str):
        # Checking if the file exist
        if not os.path.isfile(image):
            print("File {} does not exist!".format(image))
            return None
        
        # Reading image as np matrix in gray scale (image, color_param)
        return cv2.imread(image, 0)
       
    # Image alredy loaded
    elif isinstance(image, np.ndarray):
        return image
    
    return None

## To check if a number is perfect square
def is_perfect_square(x):
    if x>= 0:
        sr = int(math.sqrt(x))
        return ((sr*sr) == x)
    return False

def show_images(dir_path, image_list):
    images = []
    for image in image_list:
        image_path = os.path.join(dir_path, image)
        images.append(load_image(image_path))
        
    n: int = len(images)
    
    x = 0
    y = 0 

    if is_perfect_square(n):
        x = int(math.sqrt(n))
        y = x
    else:
        x = int(math.sqrt(n)) + 1
        y = x
        
    fig = plt.figure(figsize=(10,10))
    
    # set the timer interval 2000 milliseconds
    timer = fig.canvas.new_timer(interval = 2000)
    timer.add_callback(plt.close)
    
    for i in range(n):
        fig.add_subplot(x,y, i+1)
        plt.imshow(images[i])
    
    timer.start()
    plt.show()
        
def show_choices():
    choice = int(input("1. To Enter new Person\n2. To select existing person\n3. Discard images folder\nEnter choice : "))
    return choice

def create_new_name(dir):
    name = str(input("Enter name : "))
    
    name = name.replace(" ", "_")
    global names
    names.update({dir: name})
    
    global dest_dir
    dest_path = os.path.join('./', dest_dir)
    if name not in os.listdir(dest_path):
        os.mkdir(os.path.join(dest_path, name))
    
    global faces_dir
    dir_path = os.path.join(faces_dir, dir)
    for image_name in os.listdir(dir_path):
        image_path = os.path.join(dir_path, image_name)
        image_dest_path = os.path.join(dest_path, name)
        shutil.copy(image_path, image_dest_path)
    shutil.rmtree(dir_path)


def add_to_existing_name(dir):
    face_name = {}
    global names
    for idx,name in enumerate(names):
        print(f'{idx+1}. {names[name]}')
        face_name.update({idx:names[name]})
        
    name_idx = int(input("Enter index of existing person : "))
    name = face_name[name_idx-1]
    
    global dest_dir
    dest_path = os.path.join('./', dest_dir)
    if name not in os.listdir(dest_path):
        os.mkdir(os.path.join(dest_path, name))
        
    global faces_dir
    dir_path = os.path.join(faces_dir, dir)
    for image_name in os.listdir(dir_path):
        image_path = os.path.join(dir_path, image_name)
        image_dest_path = os.path.join(dest_path, name)
        shutil.copy(image_path, image_dest_path)
    shutil.rmtree(dir_path)

def delete_face(dir):
    global faces_dir
    dir_path = os.path.join(faces_dir, dir)
    shutil.rmtree(dir_path)

def label_face():    
    # Create final dataset folder
    global dest_dir
    dest_dir_path = os.path.join('./', dest_dir)
    if dest_dir not in os.listdir('./'):
        os.mkdir(dest_dir_path)
        
    # Label images
    global faces_dir
    for dir in os.listdir(faces_dir):
        # Current face images
        dir_path = os.path.join(faces_dir, dir)
        image_list = os.listdir(dir_path)
        
        # Show face images from current directory
        show_images(dir_path, image_list)
        
        # Ask options from user
        ch = show_choices()
        
        if ch == 1:
            create_new_name(dir)
        elif ch == 2:
            add_to_existing_name(dir)
        elif ch == 3:
            delete_face(dir)
        else:
            continue
    
    shutil.rmtree(faces_dir)