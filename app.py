from utils import image_list, create_csv, rename
from face_detection import detect, label

dest_dir = "./final-dataset"

# Get base directory input and start listing image list
base_dir = image_list.get_base_dir()
images_list = image_list.get_image_path_list(base_dir)

# Run face detection to get an unlabelled face dataset
detect.create_unlabelled_face_dataset(images_list)

# Label face images
label.label_face()

# Create csv file
rename.rename_files(dest_dir)
create_csv.create_csv(dest_dir)