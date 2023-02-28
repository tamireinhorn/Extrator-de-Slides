# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def indx():
    return render_template('index.html')

@app.route('/data')
def get_data():
    return 'Here is some data!'
if __name__ == '__main__':
    app.run()
