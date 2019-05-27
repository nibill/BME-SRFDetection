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
    image = image*mask2[:,:,np.newaxis]
    cv2.rectangle(image,(rect[0],rect[1]),(rect[2],rect[3]),(0,0,255),3)
    return image

def getGrabCutRect(image):
    candidates = []

    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            c = image[y,x]
            if c[0] <= 149 and c[0] >= 127 and c[1] <= 255 and c[1] >= 250 and c[2] <=128 and c[2] >=106:
                candidates.append([x,y])
    candidates = np.array(candidates)
    if len(candidates) != 0:
        rect = (min(candidates[:,0]),min(candidates[:,1]),max(candidates[:,0]),max(candidates[:,1]))
    else:
        rect = (0,0,image.shape[0]-1,image.shape[1]-1)
    
    return rect

def denois(image):
    return cv2.fastNlMeansDenoising(image,None,20.0,40,15) 

def reduced(image):
    Z = image.reshape((-1,3))
    # convert to np.float32
    Z = np.float32(Z)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 8
    _,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_PP_CENTERS)

    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    return res.reshape((image.shape))

def remove(image): 
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            c = image[y,x]
            if c[0] == 0 and c[1] == 0 and c[2] <=140 and c[2] >=130:
                image[y,x] = [0,0,0]
    return image