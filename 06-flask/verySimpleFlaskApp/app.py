from flask import Flask, render_template, request, json

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html', name="Maria")

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    try:
        print("Starting server...")
        app.run()
    finally:
        print("Shutting down...")
        
