import os
from flask import Flask, request, render_template
import easyocr
from PIL import Image
import warnings

UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def resize_image_if_large(image_path, max_size=(1600, 1600)):
    with Image.open(image_path) as img:
        if img.size[0] > max_size[0] or img.size[1] > max_size[1]:
            img.thumbnail(max_size)
            img.save(image_path)


warnings.filterwarnings("ignore", category=UserWarning)
reader = easyocr.Reader(['ko'], gpu = False)

@app.route("/", methods = ["GET", "POST"])
def index():
    extracted_text = ""
    corrected_text = ""
    image_path = ""
    if request.method == "POST":
        file = request.files["image"]
        if file:
            try:
                path = os.path.join(app.config['UPLOAD_FOLDER'],file.filename)
                file.save(path)
                resize_image_if_large(path)

                result = reader.readtext(path)
                extracted_text = "\n".join([text for (__, text, __) in result])
                corrected_text = extracted_text
            except Exception as e:
                print("❌ Error:", e)
                extracted_text = "Error occurred during OCR. Check console for details."


    return render_template("index.html", text=extracted_text,
                           corrected=corrected_text, image_path=image_path)
if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER, exist_ok = True)
    app.run(host='0.0.0.0', port=7860)