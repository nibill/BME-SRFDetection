import cv2

def colorMap(image) :
    im_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    im_graybi = cv2.bilateralFilter(im_gray, 9, 100, 100)
    return cv2.applyColorMap(im_graybi, cv2.COLORMAP_JET)


