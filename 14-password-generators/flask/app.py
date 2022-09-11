from os.path import join

from flask import Flask, redirect, url_for, render_template

from psw import generate_password

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate/')
def generate():
    password = generate_password()
    print(password)
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run()