import os
import csv

def create_csv(base_dir):
    label = 0
    with open('face_dataset.csv', 'w') as file:
        writer = csv.writer(file)
        for root, dirs, files in os.walk(base_dir):
            for dir in dirs:
                file_path = os.path.join(root, dir)
                for file in os.listdir(file_path):
                    fin_path = os.path.join(file_path, file)
                    writer.writerow([fin_path, label])
                label += 1