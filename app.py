import pandas as pd
from flask import Flask, render_template, json, current_app, app, request, url_for, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/model_app"
mongo = PyMongo(app)

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

@app.route("/rfmodel")
def ocr():

    model = mongo.db.model.find_one()

    data_df = pd.read_csv('modelmaker/HTRU_2.csv')
    data_df.columns = ['1','2','3','4','5','6','7','8','9']
    data_df['10'] = data_df.index
    select_df = data_df.iloc[4084:4104, 9]

    id_data = []
    d1 = {}
    for o in select_df:
        d1 = dict()
        d1['id'] = o
        id_data.append(d1)

    return render_template('rfmodel.html', data=id_data, model=model)
    

@app.route("/retrieve" , methods=['GET', 'POST'])
def retrieve():
    select = request.form.get('comp_select')
    
    model = mongo.db.model
    model_data = {'selection' : select}
    model.replace_one({},model_data, upsert=True)

    # return(model_data)
    return redirect("/rfmodel", code=302)

if __name__ == "__main__":
    app.run()

