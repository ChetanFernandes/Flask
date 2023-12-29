from flask import Flask
from flask import render_template, request, redirect
from flask import send_from_directory, abort
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

app.config["IMAGE_UPLOADS"] = "static/img"
app.config["ALLOW_IMAGE_EXTENSIONS"] = ["PNG", "JPEG", "JPG", "GIF"]
app.config["ALLOW_FILE_EXTENSIONS"] = ["TXT","xls","PY"]


def allowed_image(filename):   
    ext = filename.rsplit (".",1)[1]
    if ext.upper() in app.config["ALLOW_IMAGE_EXTENSIONS"] or ext.upper() in app.config["ALLOW_FILE_EXTENSIONS"]:
        return True
    else:
        return False

@app.route("/upload-image")
def main():

    return render_template("public/child_upload_image.html")

@app.route('/upload-image', methods=['GET', 'POST'])
def upload_file():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            if not "." in image.filename:
                print("Image must have a filename")
                return redirect("/")

            if not allowed_image(image.filename):
                return "That image extension is not allowed"
                return redirect("/")
            else:
                filename = secure_filename(image.filename)  
                image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
                ext1 = filename.rsplit (".",1)[1]
                if ext1.upper() in app.config["ALLOW_IMAGE_EXTENSIONS"]:
                    #return send_from_directory(app.config["IMAGE_UPLOADS"],filename)
                    finalimage = os.path.join(app.config["IMAGE_UPLOADS"], filename)
                    return render_template("public/child_upload_image.html", img = finalimage)
                else:
                    # To send directly from directory
                    #return send_from_directory(app.config["IMAGE_UPLOADS"],filename)
                    # To open the file and
                    file_1 = os.path.join(app.config["IMAGE_UPLOADS"], filename)
                    with open(file_1,'r') as f:
                        return render_template("public/child_upload_image.html", text = f.read())
        return render_template ("public/child_upload_image.html")

if __name__ =="__main__":
    app.run(debug = True, host = "0.0.0.0", port = 5000)