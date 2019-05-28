import cv2
import numpy as np
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

black = np.array([0, 0, 0], dtype=np.uint8)   
white = np.array([255,255,255], dtype=np.uint8)  

kLayer0 = np.array([237, 13, 0], dtype=np.uint8)   
kLayer1 = np.array([169, 255, 86], dtype=np.uint8)   
kLayer2 = np.array([ 7, 226, 247], dtype=np.uint8)   
kLayer3 = np.array([255, 125, 0], dtype=np.uint8)    
kLayer4 = np.array([ 0, 83, 253], dtype=np.uint8)    
kLayer5 = np.array([165, 0, 0], dtype=np.uint8)      
kLayer6 = np.array([245, 231, 9], dtype=np.uint8)    
kLayer7 = np.array([ 89, 255, 166], dtype=np.uint8)


kNewLayer0 = np.array([128, 0, 0], dtype=np.uint8)
kNewLayer1 = np.array([255, 209, 0], dtype=np.uint8)
kNewLayer2 = np.array([ 82, 254, 173], dtype=np.uint8)
kNewLayer3 = np.array([255, 113, 0], dtype=np.uint8)
kNewLayer4 = np.array([ 3, 240, 251], dtype=np.uint8)
kNewLayer5 = np.array([168, 255, 87], dtype=np.uint8)
kNewLayer6 = np.array([255, 66, 0], dtype=np.uint8)
kNewLayer7 = np.array([ 0, 91, 255], dtype=np.uint8)
kNewLayer8 = np.array([255, 162, 0], dtype=np.uint8)
kNewLayer9 = np.array([208, 254, 47], dtype=np.uint8)
kNewLayer10 = np.array([ 0, 172, 255], dtype=np.uint8)
kNewLayer11 = np.array([ 41, 255, 214], dtype=np.uint8)
kNewLayer12 = np.array([247, 250, 7], dtype=np.uint8)
kNewLayer13 = np.array([ 0, 9, 223], dtype=np.uint8)
kNewLayer14 = np.array([126, 255, 129], dtype=np.uint8)
kNewLayer15 = np.array([243, 10, 0], dtype=np.uint8)

kCenters = np.array([kLayer0,kLayer1,kLayer2,kLayer3,kLayer4,kLayer5,kLayer6,kLayer7], dtype=np.uint8)

kNewCenters = np.array([kNewLayer0,kNewLayer1,kNewLayer2,kNewLayer3,kNewLayer4,kNewLayer5,kNewLayer6,kNewLayer7,kNewLayer8,kNewLayer9,kNewLayer10,kNewLayer11,kNewLayer12,kNewLayer13,kNewLayer14,kNewLayer15], dtype=np.uint8)

def colorMap(image) :
    return cv2.applyColorMap(image, cv2.COLORMAP_JET)

     

def grabCut(image):
    image[np.where((image == kLayer5).all(axis = 2))] = [0,0,0]

    return image

def getGrabCutRect(image):
    rect = (0,0,image.shape[0],image.shape[1])
    
    return rect

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
    for i in range(len(center)):
        dist = np.inf
        ind = 0
        for j in range(len(kCenters)):
            a = convert_color(sRGBColor(center[i][2],center[i][1],center[i][0]), LabColor)
            b = convert_color(sRGBColor(kCenters[j][2],kCenters[j][1],kCenters[j][0]), LabColor)
            d = delta_e_cie2000(a, b)
            if dist > d:
                dist = d
                ind = j
        center[i] = kCenters[ind]
    res = center[label.flatten()]
    return res.reshape((image.shape))

def open(image):
    kernel = np.ones((15,15),np.uint8)
    opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    return opening

def clean(image):
    for y in reversed(range(image.shape[0])):
        o = len(image[y])
        c = len(image[y][np.where((image[y] == [0,0,0]).all(axis = 1))])
        if o == c:
            image = np.delete(image, (y), axis=0)

    for x in reversed(range(image.shape[1])):
        o = len(image[:,x])
        c = len(image[:,x][np.where((image[:,x] == [0,0,0]).all(axis = 1))])
        if o == c:
            image = np.delete(image, (x), axis=1)
    
    return image

def newMask(image):
    image[np.where((image == kLayer0).all(axis = 2))] = white
    image[np.where((image == kLayer1).all(axis = 2))] = white
    image[np.where((image == kLayer2).all(axis = 2))] = white
    image[np.where((image == kLayer3).all(axis = 2))] = white
    image[np.where((image == kLayer4).all(axis = 2))] = white
    image[np.where((image == kLayer5).all(axis = 2))] = white
    image[np.where((image == kLayer6).all(axis = 2))] = white
    image[np.where((image == kLayer7).all(axis = 2))] = white
     
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    _,contours,_ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(image, contours, -1, (255,255,255), thickness=-1)

    kernel = np.ones((63,63),np.uint8)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

    return image

def newImage(mask,image):
    mask[np.where((mask == white).all(axis = 2))] = 1
    mask[np.where((mask == black).all(axis = 2))] = 0

    return image * mask

def reduced2(mask,image):
    Z = image.reshape((-1,3))
    # convert to np.float32
    Z = np.float32(Z)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 16
    _,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_PP_CENTERS)

    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    for i in range(len(center)):
        dist = np.inf
        ind = 0
        for j in range(len(kNewCenters)):
            a = convert_color(sRGBColor(center[i][2],center[i][1],center[i][0]), LabColor)
            b = convert_color(sRGBColor(kNewCenters[j][2],kNewCenters[j][1],kNewCenters[j][0]), LabColor)
            d = delta_e_cie2000(a, b)
            if dist > d:
                dist = d
                ind = j
        center[i] = kNewCenters[ind]
    res = center[label.flatten()]
    image = res.reshape((image.shape))

    mask[np.where((mask == white).all(axis = 2))] = 1
    mask[np.where((mask == black).all(axis = 2))] = 0

    return image * mask

def lineSegment(image):
    sub = colorPicked(image,kNewLayer13, kNewLayer4)
    image = sub + colorPicked(image,kNewLayer2, kNewLayer2)
    return image

def colorPicked(image, lower, upper):
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    mask = cv2.inRange(image, lower, upper)
    image = cv2.bitwise_and(image, image, mask=mask)

    return image

def hough(image,prev):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (9, 9), 1.1)

    edges = cv2.Canny(gray, 75, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi/90, 110, minLineLength=10, maxLineGap=50)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 10)

    kernel = np.ones((63,63),np.uint8)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, image = cv2.threshold(image, 1, 255, cv2.THRESH_BINARY)

    mask = prev.copy()

    for x in range(image.shape[1]):
        indices = [i for i, x in enumerate(image[:,x]) if x == 255]
        if len(indices) == 0:
            mask[:,x] = 0
            continue
        amin = min(indices)
        amax = max(indices)

        mask[:,x] = 0
        mask[:,x][(amax-amin)//2+amin:amax] = 1
    return prev * mask,mask

def count(image):
    blue = len(image[np.where((image == kNewLayer0).all(axis = 2))]) 
    blue = blue + len(image[np.where((image == kNewLayer15).all(axis = 2))])
    gray_image = cv2.cvtColor(colorPicked(image,kNewLayer13, kNewLayer4), cv2.COLOR_BGR2GRAY)
    red = cv2.countNonZero(gray_image)

    percent = np.inf
    if blue != 0 and red != 0:
        percent = blue/red
        
    return [blue,red,percent]

def hough2(image,prev,maskPrev):
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # gray = cv2.GaussianBlur(gray, (9, 9), 2)

    # edges = cv2.Canny(gray, 75, 150)
    # lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, minLineLength=10, maxLineGap=50)
    # if lines is not None:
    #     for line in lines:
    #         x1, y1, x2, y2 = line[0]
    #         cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 10)

    # kernel = np.ones((63,63),np.uint8)
    # image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    mask = maskPrev.copy()
    image = prev * maskPrev
    image = lineSegment(image)

    kernel = np.ones((63,63),np.uint8)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    #return image,mask
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, image = cv2.threshold(image, 1, 255, cv2.THRESH_BINARY)

    for x in range(image.shape[1]):
        indices = [i for i, x in enumerate(image[:,x]) if x == 255]
        if len(indices) == 0:
            mask[:,x] = 0
            continue
        amin = int(min(indices))
        amax = int(max(indices))

        mask[:,x] = 0
        mask[:,x][amin:amax] = 1

    image = prev * mask
    return image,mask
