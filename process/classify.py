import process.image

def classify(image_struc) :

    denoised = process.image.denois(image_struc[1])
    colorMap = process.image.colorMap(denoised)
    reduced = process.image.reduced(colorMap)
    remove = process.image.remove(reduced)
    grabCut = process.image.grabCut(remove)

    result = "SRF"

    return [image_struc[0],result,image_struc[1],denoised,colorMap,reduced,grabCut]