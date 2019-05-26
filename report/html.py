import cv2
import base64

def insert_into_template(string,title) :
    start = """<!doctype html>
    <html lang="en">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

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

    return start + string + end

def create_html(result) :
    
    images = ""

    for item in result :
        images += "<tr>"
        images += "<td>" + item[0] + "</td>"
        images += "<td>" + item[1] + "</td>"
        images += "<td>" + "<img src=\"data:image/gif;base64," + imageToBase64(item[2]) + "\"></td>"
        images += "<td>" + "<img src=\"data:image/gif;base64," + imageToBase64(item[3]) + "\"></td>"
        images += "<td>" + "<img src=\"data:image/gif;base64," + imageToBase64(item[4]) + "\"></td>"
        images += "</tr>"

    images = "<table class=\"table\">" + images + "</table>"

    return  insert_into_template(images,"Images")


def imageToBase64(image) :
    img_str = cv2.imencode('.png', image)[1].tostring()
    return base64.b64encode(img_str).decode("utf-8") 
    