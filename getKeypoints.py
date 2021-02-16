import os
import threading
import json
from classes import Keypoint

def wait_for_frames():
    while not os.path.isdir('keypoints/run0'):
        print("waiting for frame dir, pls start openpose")
    print("dir detected!")
    while len(os.listdir("keypoints/run0")) == 0:
        print("dir empty, waiting for frames")
    print("frame detected!")

def get_frames():
    return os.listdir("keypoints/run0")

def collect_keypoints(frame):
    os.chdir("keypoints/run0")
    # read json file
    with open(frame, 'r') as frame:
        data=frame.read()
    # parse file
    obj = json.loads(data)
    # get raw keypoints list
    if not obj['people']:
        os.chdir("../..")
        print("No people found")
        return []
    else:
        keypoints_face_raw = obj['people'][0]['face_keypoints_2d']
        os.chdir("../..")
        print("collected keypoints succesfully!")
        return keypoints_face_raw
    

def filter_keypoints(keypoints_face_raw):
    # filter different values
    x_positions = keypoints_face_raw[::3]
    y_positions = keypoints_face_raw[1::3]
    c_values = keypoints_face_raw[2::3]

    # generate keypoints list
    keypoints_face = []
    for (x, y, c) in zip(x_positions, y_positions, c_values):
      keypoints_face.append(Keypoint(x, y, c))

    # filter different features
    keypoints_eyebrows = keypoints_face[17:27]
    keypoints_nosebridge = keypoints_face[27:31]
    keypoints_nostrils = keypoints_face[31:36]
    keypoints_eyes = keypoints_face[36:48]
    keypoints_mouth = keypoints_face[48:68]
    # log
    print("filtered keypoints succesfully!")
    return keypoints_eyebrows, keypoints_nosebridge, keypoints_nostrils, keypoints_eyes, keypoints_mouth



