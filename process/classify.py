import process.image

def classify(image_struc) :

    colorMap = process.image.colorMap(image_struc[1])

    result = "SRF"

    return [image_struc[0],result,image_struc[1],colorMap]