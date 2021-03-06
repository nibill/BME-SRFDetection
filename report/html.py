import cv2
import base64
import numpy as np

def insert_into_template(string,title) :
    start = """<!doctype html>
    <html lang="en">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

        <style>
            img {
                max-height:250px; width:auto
                }
        </style>
    """
    mid = """
        <title>{title}</title>
    </head>
    <body>
        <h1>{title}</h1>
    """.format(title=title)
    end = """
        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    </body>
    </html>"""

    return start + mid + string + end

def create_html(result,evaluation) :
    
    images = ""

    for item in result :
        images += "<tr>"
        images += "<td>" + item[0] + "</td>"
        images += "<td>" + item[1] + "</td>"
        images += "<td>" + item[2] + "</td>"
        images += "<td>" + "<img src=\"data:image/gif;base64," + imageToBase64(item[4]) + "\"></td>"
        images += "<td>" + "<img src=\"data:image/gif;base64," + imageToBase64(item[5]) + "\"></td>"
        images += "<td>" + "<img src=\"data:image/gif;base64," + imageToBase64(item[6]) + "\"></td>"
        images += "<td>" + "<img src=\"data:image/gif;base64," + imageToBase64(item[7]) + "\"></td>"
        images += "<td>" + "<img src=\"data:image/gif;base64," + imageToBase64(item[8]) + "\"></td>"
        images += "<td>" + "<img src=\"data:image/gif;base64," + imageToBase64(item[9]) + "\"></td>"
        images += "<td>" + "<img src=\"data:image/gif;base64," + imageToBase64(item[10]) + "\"></td>"
        images += "<td>" + "<img src=\"data:image/gif;base64," + imageToBase64(item[11]) + "\"></td>"
        images += "<td>" + "<img src=\"data:image/gif;base64," + imageToBase64(item[12]) + "\"></td>"
        images += "<td>" + "<img src=\"data:image/gif;base64," + imageToBase64(item[13]) + "\"></td>"
        images += "<td>" + "<img src=\"data:image/gif;base64," + imageToBase64(item[14]) + "\"></td>"
        images += "<td>" + "<img src=\"data:image/gif;base64," + imageToBase64(item[15]) + "\"></td>"
        images += "<td> blue: " + str(item[3][0]) + " red: " + str(item[3][1]) + " percent: " + str(item[3][2]) + "</td>"
        images += "<td>" + item[1] + "</td>"
        images += "<td>" + item[2] + "</td>"
        images += "</tr>"

    images = "<table class=\"table\">" + images + "</table>"

    return  insert_into_template(images,"Result " + str(evaluation[0]) )


def imageToBase64(image) :
    if isinstance(image, np.ndarray) == False:
        return ""
    img_str = cv2.imencode('.png', image)[1].tostring()
    return base64.b64encode(img_str).decode("utf-8") 
    