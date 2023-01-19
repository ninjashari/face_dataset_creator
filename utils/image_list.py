import os

def get_base_dir() -> str:
    base_dir = str(input("Enter full path of root directory of images\n"))
    if base_dir is not None and len(base_dir)>0:
        return base_dir
    else:
        print("Base directory entered is invalid\nExiting program...")
        exit()

def get_image_path_list(base_dir: str):
    path_list = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            path_list.append(os.path.join(root,file))
    return path_list