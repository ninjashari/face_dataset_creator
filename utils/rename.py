import os

def rename_files(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            for idx, file in enumerate(os.listdir(dir_path)):
                file_path = os.path.join(root, dir, file)
                new_path = os.path.join(root, dir, dir + '_' + str(idx) + '.png')                
                os.rename(file_path, new_path)