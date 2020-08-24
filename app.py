from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def data():
    return render_template("data.html")

@app.route("/credits")
def credits():
    return render_template("credits.html")

@app.route("/charts")
def charts():
    return render_template("charts.html")

@app.route("/randomforest")
def randomforest():
    return render_template("randomforest.html")


if __name__ == "__main__":
    app.run()

