import os
import cv2

def load(path) :
    files = []
    for r, _, f in os.walk(path):
        for file in f:
            if '.png' in file:
                fullpath = os.path.join(r, file)
                files.append([os.path.basename(os.path.dirname(fullpath)), cv2.imread(fullpath)])
    return files