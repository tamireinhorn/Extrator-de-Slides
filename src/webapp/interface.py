from flask import Flask, request, render_template, send_file
import os
from ExtratorSlides.SlideExtractor import video_processing, choose_video

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/upload", methods=["POST"])
def upload():
    try:
        slide_length = int(request.form['slide_length'])
        video_file = choose_video()
        pdf_path = video_processing(video_file, slide_length)
        return send_file(pdf_path, attachment_filename=os.path.basename(pdf_path))
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
