import process.image

def classify(image_struc) :
    image = image_struc[1][14:image_struc[1].shape[0]-34,47:image_struc[1].shape[1]-11]

    openi = process.image.open(image.copy())
    colorMap = process.image.colorMap(openi.copy())
    reduced = process.image.reduced(colorMap.copy())
    grabCut = process.image.grabCut(reduced.copy())
    newMask = process.image.newMask(grabCut.copy())
    newImage = process.image.newImage(newMask.copy(),image.copy())

    colorMap2 = process.image.colorMap(newImage.copy())
    reduced2 = process.image.reduced2(newMask.copy(),colorMap2.copy())
    clean = process.image.clean(reduced2.copy())
    lineSegment = process.image.lineSegment(clean.copy())
    hough,mask = process.image.hough(lineSegment.copy(),clean.copy())
    hough2,_ = process.image.hough2(lineSegment.copy(),clean.copy(),mask.copy())

    count = process.image.count(hough.copy())

    result = ""

    return [image_struc[2],image_struc[0],result,count,image,openi,colorMap,reduced,grabCut,newMask,newImage,reduced2,clean,lineSegment,hough,hough2]