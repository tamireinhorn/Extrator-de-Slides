from flask import Flask, request, render_template, send_file
from ExtratorSlides.SlideExtractor import *
import numpy as np
from pathlib import Path
import shutil
import cv2
import tempfile
import os

os.makedirs("extractor", exist_ok=True)
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/upload", methods=["POST"])
def upload():
    video_file = request.files["video"]
    iterations = request.form["slide-number"]
    try:

        with tempfile.TemporaryDirectory(
            dir="extractor", ignore_cleanup_errors=True
        ) as td:
            print("Temporary directory created at:", td)
            temp_filename = Path(td) / "uploaded_video"
            validate_video(video_file.filename)
            video_file.save(temp_filename)
            video = cv2.VideoCapture(str(temp_filename))
            video_length = calculate_length_video(video)
            video.release()
            return "And it finally worked."
    except Exception as e:
        return render_template("error.html", message=str(e))
    finally:
        shutil.rmtree(td, ignore_errors=True)


if __name__ == "__main__":
    app.run(debug=True)
