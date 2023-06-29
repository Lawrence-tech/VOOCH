import os
from flask import Flask, render_template, request, redirect, session
from werkzeug.utils import secure_filename
app = Flask(__name__)

upload_path = os.path.join('static/uploads')
print(upload_path)
app.config["UPLOADS"] = upload_path
app.config["ALLOWED_FILE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF", "jpg"]
# Define a secret key to enable session
app.secret_key = os.environ.get("APP_SECRET_KEY", "default_secret_key")


@app.route("/", strict_slashes=False)
def default():
    """Default route"""
    return render_template('upload.html')


def allowed_file(filename):
    """check if the file extension is allowed"""

    if "." not in filename:
        return False

    exten = filename.rsplit(".", 1)[1]

    if exten.upper() in app.config["ALLOWED_FILE_EXTENSIONS"]:
        return True
    else:
        return False


@app.route("/", strict_slashes=False, methods=["GET", "POST"])
def upload_file():
    """defines upload file route"""
    if request.method == "POST":
        if request.files:
            f = request.files["uploaded-file"]
            if f.filename == "":
                print("No filename")
                return redirect(request.url)

            if allowed_file(f.filename):
                filename = secure_filename(f.filename)
                f.save(os.path.join(app.config["UPLOADS"], filename))
                image_path = os.path.join(app.config["UPLOADS"], filename)
                # store image_path in session
                session["image_path"] = image_path
                print("File saved")
                return render_template('upload2.html')
            else:
                print("File exetension is not allowed")
                return redirect(request.url)
    return render_template('upload.html')


@app.route("/image_display", strict_slashes=False)
def show_image():
    """Displays the uploaded Image"""
    # Retrive image_path from session
    image_path = session.get("image_path")
    print(image_path)
    if image_path:
        return render_template('image_diplay.html', user_image=image_path)
    else:
        return "Image not found"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
