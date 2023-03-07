from flask import Flask, request, render_template, send_file


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/upload", methods=["POST"])
def process_video():
    pass


if __name__ == "__main__":
    app.run(debug=True)
