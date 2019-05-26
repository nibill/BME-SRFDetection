import process.image

def classify(image_struc) :

    denoised = process.image.denois(image_struc[1])
    colorMap = process.image.colorMap(denoised)
    grabCut = process.image.grabCut(colorMap)
    hardColor = process.image.hardColor(grabCut)

    result = "SRF"

    return [image_struc[0],result,image_struc[1],denoised,colorMap,grabCut,hardColor]