import os
import cv2
import face_recognition

names = []
name_count = {}
known_faces = []

dataset_dest = "face-dataset"

def create_new_face(face_location, image_file, face_name, face_encoding):
    # Location of each face in this image file
    top, right, bottom, left = face_location
    
    # # Access the actual face
    face_image = image_file[top:bottom, left:right]
    
    global names
    names.append(face_name)
    
    global name_count
    name_count.update({face_name: 1})
    
    global known_faces
    known_faces.append(face_encoding)
    
    # Create face-dataset folder
    global dataset_dest
    if dataset_dest not in os.listdir("./"):
        os.mkdir(dataset_dest)
        
    # Create face-name folder
    # print(os.getcwd)
    dest_path = os.path.join('./', dataset_dest)
    final_dest_path = os.path.join(dest_path, face_name)
    
    if face_name not in os.listdir('./'):
        os.mkdir(final_dest_path)
    
    # Image file-name
    image_file_name = str(face_name) + '_' + str(name_count[face_name]) + ".png"
    image_file_path = os.path.join(final_dest_path, image_file_name)
    
    # Write the face-image-file
    cv2.imwrite(image_file_path, face_image)
    
    name_count[face_name] += 1
    
def create_unlabelled_face_dataset(image_path_list):
    count = 0
    for image_path in image_path_list:
        # Load the image file
        print(f'Current image : {image_path}')
        image_file = face_recognition.load_image_file(image_path)
    
        # Find all faces and face encodings in current image
        face_locations = face_recognition.face_locations(image_file, number_of_times_to_upsample=0, model='cnn')
        face_encodings = face_recognition.face_encodings(image_file, face_locations)
        
        for i in range(len(face_encodings)):
            # Check if face is match for known faces
            if len(known_faces) > 0:
                match = face_recognition.compare_faces(known_faces, face_encodings[i], tolerance=0.4)
                
                match_flag = False
                match_idx = None
                 
                # Check if match array represents any known face 
                for j in range(len(match)):
                    if match[j]:
                        match_flag = True
                        match_idx = j
                        break
                    
                if match_flag:
                    # Add face to dataset
                    # Location of each face in this image
                    top, right, bottom, left = face_locations[i]
                    
                    # Access actual face
                    face_image = image_file[top:bottom, left:right]
                    
                    # Add image to folder
                    global names
                    dest_path = os.path.join(dataset_dest, names[match_idx])
                    final_dest_path = os.path.join('./', dest_path)
                    
                    # Image file-name
                    image_file_name = str(names[match_idx]) + '_' + str(name_count[names[match_idx]]) + ".png"
                    image_file_path = os.path.join(final_dest_path, image_file_name)
                    cv2.imwrite(image_file_path, face_image)
                    
                    name_count[names[match_idx]] += 1
                else:
                    face_name = "Person_" + str(count)
                    count += 1
                    create_new_face(face_locations[i], image_file, face_name, face_encodings[i])
            else:
                face_name = "Person_" + str(count)
                count += 1
                create_new_face(face_locations[i], image_file, face_name, face_encodings[i])
        
        print("Found {} face(s) in this image.".format(len(face_locations)))