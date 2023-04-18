import os
import pathlib
import pytesseract  
from PIL import Image 
from googletrans import Translator
from flask import Flask, url_for, redirect,  render_template, request

SRC_PATH =  pathlib.Path(__file__).parent.absolute()
UPLOAD_FOLDER = os.path.join(SRC_PATH,  'static', 'uploads')

app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/ocr', methods=['POST'])
def upload_file():
    file = request.files['filename']
    if file.filename != '':
        file.save(os.path.join(UPLOAD_FOLDER, 'text.jpg'))
    image = Image.open("D:/photoshare/src/static/uploads/text.jpg")
    text = pytesseract.image_to_string(image,lang='eng')
    translator = Translator()
    language = request.form.get('language')
    translated_text = translator.translate(text, dest=language).text
    return '''
        <html>
            <body>
                <img src="static/uploads/text.jpg">
                <br>
                <pre style="font-size: 18px;">{}</pre>
            </body>
        </html>
    '''.format(translated_text)

if __name__ == "__main__":
    app.run()