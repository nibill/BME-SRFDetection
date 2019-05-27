import cv2
import numpy as np

def colorMap(image) :
    im_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    im_graybi = cv2.bilateralFilter(im_gray, 9, 100, 100)
    return  cv2.applyColorMap(im_graybi, cv2.COLORMAP_JET)

def grabCut(image):
    mask = np.zeros(image.shape[:2],np.uint8)
    
    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)

    rect = getGrabCutRect(image)
    cv2.grabCut(image,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')

    return image*mask2[:,:,np.newaxis]

def getGrabCutRect(image):
    candidates = []
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            c = image[y,x]
            if c[2] > 100 and c[2] < 180 and c[1] == 255 and c[0] > 150 and c[0] < 200:
                candidates.append([x,y])
    candidates = np.array(candidates)

    rect = (min(candidates[:,0]),min(candidates[:,1]),max(candidates[:,0]),max(candidates[:,1]))

    return rect

def denois(image):
    return cv2.fastNlMeansDenoising(image,None,20.0,40,15) 

def hardColor(image):
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            c = image[y,x]
            if c[2] > 0 and c[2] < 10 and c[1] == 0 and c[0] > 240 and c[0] < 250:
                image[y,x][0] = 0
                image[y,x][1] = 0
                image[y,x][2] = 0

    return image

def open(image):
    kernel = np.ones((5,5),np.uint8)
    opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    return opening