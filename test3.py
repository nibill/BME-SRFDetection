import numpy as np
import matplotlib.pylab as plt
import os

cwd = os.getcwd()
file_name = os.path.join(cwd, "/Repos/BME-SRFDetection/Data/SRF/input_1492_1.png")

im = plt.imread(file_name)
im

