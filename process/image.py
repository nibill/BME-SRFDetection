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

    rect = getGrabCutRect(image) #(0, image.shape[:2][0]//2, image.shape[:2][1], image.shape[:2][0])
    cv2.grabCut(image,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')

    return image*mask2[:,:,np.newaxis]

def getGrabCutRect(image):
    candidates = []
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            c = image[y,x]
            if c[2] > 75 and c[2] < 200 and c[1] == 255 and c[0] > 120 and c[0] < 220:
                candidates.append([x,y])
    candidates = np.array(candidates)

    rect = (min(candidates[:,0]),min(candidates[:,1]),max(candidates[:,0]),max(candidates[:,1]))

    #print(rect)
    return rect

def denois(image):
    return cv2.fastNlMeansDenoising(image,None,20.0,40,15) 