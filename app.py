from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        if not request.form.get("name") or not request.form.get("email"):
            return ("Please fill input approprately")
        return render_template("certificate.html", name=request.form.get("name", "world"))
