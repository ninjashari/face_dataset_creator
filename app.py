from image_list import images
from face_detection import detect, label

# Get base directory input and start listing image list
base_dir = images.get_base_dir()
images_list = images.get_image_path_list(base_dir)

# Run face detection to get an unlabelled face dataset
detect.create_unlabelled_face_dataset(images_list)

# Label face images
label.label_face()