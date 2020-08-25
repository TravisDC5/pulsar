import os
from flask import Flask, render_template, json, current_app, app, request, \
    url_for, redirect

# static/data/test_data.json
# dataFile = os.path.join(app.static_folder, 'data', 'test_data.json')

# with open(dataFile) as test_file:
#     data = json.load(test_file)

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

@app.route("/ocr")
def ocr():
     return render_template('ocr.html',
        data=[{'name':'red'}, {'name':'green'}, {'name':'blue'}])

@app.route("/model" , methods=['GET', 'POST'])
def model():
    select = request.form.get('comp_select')
    return(str(select)) # just to see what select is

if __name__ == "__main__":
    app.run()

