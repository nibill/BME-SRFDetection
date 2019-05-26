import numpy as np
import matplotlib.pylab as plt
import cv2
import os

cwd = os.getcwd()
file_name = os.path.join(cwd, "/Repos/BME-SRFDetection/Data/SRF/input_1647_1.png")

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]

oct = cv2.imread(file_name,2)

ret, oct_bin = cv2.threshold(oct,100,255,cv2.THRESH_BINARY)

bright_blue = (68, 1, 84)
dark_blue = (253, 231, 36)


#mask = cv2.inRange(oct_bin, bright_blue, dark_blue)
#result = cv2.bitwise_and(oct_bin, oct_bin, mask=mask)



plt.imshow(oct_bin)
plt.show()

