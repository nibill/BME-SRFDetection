# import numpy as np
# import matplotlib.pyplot as plt
# from skimage.color import rgb2gray
# from skimage import data
# from skimage.filters import gaussian
# from skimage.segmentation import active_contour
# from skimage import io
# import os
# import cv2




# cwd = os.getcwd()
# file_name = os.path.join(cwd, "/Repos/BME-SRFDetection/Data/SRF/input_1492_1.png")

# img = io.imread(file_name)

# img = rgb2gray(img)

# im_gray = cv2.imread(file_name)
# im_graybi = cv2.bilateralFilter(im_gray, 9, 100, 100)
# img = cv2.applyColorMap(im_gray, cv2.COLORMAP_JET)

# s = np.linspace(0, 2*np.pi, 400)
# x = 290 + 100*np.cos(s)
# y = 230 + 60*np.sin(s)
# init = np.array([x, y]).T

# snake = active_contour(gaussian(img, 3),
#                        init, alpha=0.02, beta=30, gamma=0.001)

# fig, ax = plt.subplots(figsize=(7, 7))
# ax.imshow(img, cmap=plt.cm.gray)
# ax.plot(init[:, 0], init[:, 1], '--r', lw=3)
# ax.plot(snake[:, 0], snake[:, 1], '-b', lw=3)
# ax.set_xticks([]), ax.set_yticks([])
# ax.axis([0, img.shape[1], img.shape[0], 0])

# plt.show()

from skimage import io as sio
import skimage
import os
import cv2
import numpy as np
import argparse
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


file_name = os.getcwd() + "/Data/SRF/input_1492_1.png" #os.path.join(cwd, "/Repos/BME-SRFDetection/Data/SRF/input_1492_1.png")

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