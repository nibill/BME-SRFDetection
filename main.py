from skimage import io as sio
import skimage
import os
import cv2
import numpy as np
import argparse
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


cwd = os.getcwd()
file_name = os.path.join(cwd, "/Repos/BME-SRFDetection/Data/SRF/input_1492_1.png")

#im_gray = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
im_gray = cv2.imread(file_name)

im_graygauss = cv2.GaussianBlur(im_gray, (7, 7), 2)
im_colorgauss = cv2.applyColorMap(im_graygauss, cv2.COLORMAP_JET)

im_graybi = cv2.bilateralFilter(im_gray, 9, 100, 100)
im_colorbi = cv2.applyColorMap(im_graybi, cv2.COLORMAP_JET)


f = plt.figure()
f.add_subplot(2, 2, 1)
plt.imshow(im_gray)
f.add_subplot(2, 2, 2)
plt.imshow(im_colorbi)
f.add_subplot(2, 2, 3)
plt.imshow(im_colorgauss)
plt.show(block=True)
