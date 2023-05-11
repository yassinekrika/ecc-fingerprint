import cv2
import numpy as np

def fingerprint(path):
    img = cv2.imread(path, 0)

    img = cv2.equalizeHist(img)

    sift = cv2.SIFT_create()

    keypoints, descriptions = sift.detectAndCompute(img, None)

    feature_vector = descriptions.flatten()

    vector = np.array(descriptions).flatten()

    empty_str = ''
    for i in vector:
        empty_str = empty_str + str(int(i))
     
    return int(empty_str)