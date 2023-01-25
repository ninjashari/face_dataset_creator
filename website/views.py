import os
from utils import image_list, create_csv, rename
from face_detection import detect, label
from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'folder_path' in request.form:
            folder_path = request.form['folder_path']
        if os.path.exists(folder_path):
            images_list = image_list.get_image_path_list(folder_path)
            print(images_list)
            # Run face detection to get an unlabelled face dataset
            detect.create_unlabelled_face_dataset(images_list)
        else :
            print(f'Error :: Path does not exist or invalid')
    return render_template('home.html')

@views.route('/unlabel', methods=['GET', 'POST'])
def faces_creation():
    return render_template('unlabel.html')
    