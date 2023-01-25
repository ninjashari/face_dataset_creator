import os

def get_image_path_list(base_dir: str):
    path_list = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            path_list.append(os.path.join(root,file))
    return path_list