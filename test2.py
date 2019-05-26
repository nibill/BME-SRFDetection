import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import data
from skimage.filters import gaussian
from skimage.segmentation import active_contour
import skimage.segmentation as seg
from skimage import io
import os
import cv2

import skimage.color as color

def image_show(image, nrows=1, ncols=1, cmap='gray'):
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(14, 14))
    ax.imshow(image, cmap='gray')
    ax.axis('off')
    return fig, ax

cwd = os.getcwd()
file_name = os.path.join(cwd, "/Repos/BME-SRFDetection/Data/SRF/input_1492_1.png")

im_gray = cv2.imread(file_name)
#im_graybi = cv2.bilateralFilter(im_gray, 9, 100, 100)
img = cv2.applyColorMap(im_gray, cv2.COLORMAP_JET)

image_slic = seg.slic(img,n_segments=155)
image_show(color.label2rgb(image_slic, img, kind='avg'));