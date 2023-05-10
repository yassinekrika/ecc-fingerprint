import cv2
import numpy as np

def fingerprint():
    img = cv2.imread('/home/yassg4mer/Project/ecc_finger_print/client/public/fingerprint-reader.jpg', 0)

    img = cv2.equalizeHist(img)

    sift = cv2.SIFT_create()

    keypoints, descriptions = sift.detectAndCompute(img, None)

    feature_vector = descriptions.flatten()

    vector = np.array(descriptions).flatten()
     
    return vector