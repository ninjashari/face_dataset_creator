# Face Dataset Creator

Detect faces from your personal images and create a dataset for face recognition.

## Features

1. **Detect and extract faces from images**
2. **Label/Discard your each set of faces**
3. **Generate a labeled dataset of faces and a csv file**

## Installation instructions
### Linux operating system is preferred

1. Install miniconda

    `curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64 sh -o Miniconda3-latest-Linux-x86_64.sh`

    `bash Miniconda3-latest-Linux-x86_64.sh`
    
2. For GPU based runtime

    1. Install Nvidia drivers
        [Nvidia Drivers](https://www.nvidia.com/drivers)
    2. Install CUDA toolkit (Recommended version : 11.2)
        [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit-archive)
    3. Install cuDNN SDK (Recommended version : 8.1.0)
        [cuDNN SDK](https://developer.nvidia.com/cudnn)

3. Create a new env using miniconda

    `conda create --name newenv python=3.9`

4. Make and install dlib [From [source](https://github.com/davisking/dlib) is prefered]
    1. Use gcc-10 to build dlib with CUDA Toolkit v11.2
    2. Set appropriate flags for dlib to use CUDA

5. Install Face Recognition library
    1. Link - [face_recognition](https://github.com/ageitgey/face_recognition)
    2. Command - `pip install face-recognition`
    3. [pypi link](https://pypi.org/project/face-recognition/)

