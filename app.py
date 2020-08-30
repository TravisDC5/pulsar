import pandas as pd
import numpy as np
import pickle
from flask import Flask, render_template, json, current_app, app, request, url_for, redirect
from flask_pymongo import PyMongo


app = Flask(__name__)

# app.config["MONGO_URI"] = "mongodb://localhost:27017/model_app"
app.config["MONGO_URI"] = "mongodb+srv://admin:orangepeal1@cluster0.zr2qk.mongodb.net/model_app?retryWrites=true&w=majority"
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

@app.route("/nnet")
def nnet():
    return render_template("neuralNet.html")

@app.route("/roc")
def randomforest():
    return render_template("rocChart.html")

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

    data = pd.read_csv('modelmaker/HTRU_2.csv')
    data.columns = ['1','2','3','4','5','6','7','8','9']
    data['10'] = data.index


    spam = data[(data['10'] >= 4084) & (data['10'] <= 4103)]
    spam2 = data[(data['9'] >= 4084) & (data['9'] <= 4103)]

    temp = spam['10'] == int(select)

    temp2 = spam[temp]
    temp3 = temp2["9"].values[0]
    cla = ""
    if temp3 == 0:
        cla = "Not a Pulsar"
    else:
        cla = "Is a Pulsar"

    pickle_file = "modelmaker/RFC_model_v1_12_3_175.h5"

    with open(pickle_file, 'rb') as file:
        Pickled_RF_Model = pickle.load(file)

    X = temp2.iloc[:,:-2].values
    y = temp2.iloc[:,-2].values

    y_pred = Pickled_RF_Model.predict(X)

    if y_pred[0] == 0:
        model_output = "Not a Pulsar"
    else:
        model_output = "Is a Pulsar"
    # print(model_output)


    model = mongo.db.model
    model_data = {'selection' : select, 'class_acc': cla, 'class_pre': model_output}
    model.replace_one({},model_data, upsert=True)


    return redirect("/rfmodel", code=302)

@app.route("/retrieve2" , methods=['GET', 'POST'])
def retrieve2():
    model = mongo.db.model.find_one()
    
    fname = request.form.get('fname')
    age = request.form.get('age')
    sibling = request.form.get('sibling')
    pets = request.form.get('pets')
    origin = request.form.get('origin')
    city = request.form.get('city')
    hours = request.form.get('hours')
    pnumber = request.form.get('pnumber')

    # Get Ascii values for name
    nameValue = fname
    ascValue = []

    for name in nameValue:
        for ch in name:
            ascValue.append(ord(ch))

    charCount = len(ascValue)
    valSum = sum(ascValue)

    fnameValue = round(valSum/charCount,2)
    
    # Get Ascii values for origin
    originValue = origin
    ascValue2 = []

    for name in originValue:
        for ch in name:
            ascValue2.append(ord(ch))

    charCount2 = len(ascValue2)
    valSum2 = sum(ascValue2)

    originValueAsc = round(valSum2/charCount2,2)

    # Get Ascii values for currenct city
    cityValue = city
    ascValue3 = []

    for name in cityValue:
        for ch in name:
            ascValue3.append(ord(ch))

    charCount3 = len(ascValue3)
    valSum3 = sum(ascValue3)

    cityValueAsc = round(valSum3/charCount3,2)
    
    # Run Data through Model
    dataArray = np.array([fnameValue, age, sibling, pets, originValueAsc, cityValueAsc, hours, pnumber] , dtype=float)
    print(dataArray)
    pickle_file = "modelmaker/RFC_model_v1_12_3_175.h5"

    with open(pickle_file, 'rb') as file:
        Pickled_RF_Model = pickle.load(file)
    
    X = dataArray
    X = X.reshape(-1,1)
    
    y_pred = Pickled_RF_Model.predict(X)

    if y_pred[0] == 0:
        model_output2 = "Not a Pulsar"
    else:
        model_output2 = "a Pulsar"

    
    model = mongo.db.model
    model_data = {'firstName' : fname,
                  'personAge': age, 
                  'nameValueAVG': fnameValue,
                  'sibCount': sibling,
                  'numPets': pets,
                  'origin': origin,
                  'originValueAsc': originValueAsc,
                  'currCity': city,
                  'cityValueAsc': cityValueAsc,
                  'labHours': hours,
                  'favNumber': pnumber,
                  'humanPulsar': model_output2
                  }
    model.replace_one({},model_data, upsert=True)

    return redirect("/rfmodel", code=302)

if __name__ == "__main__":
    app.run()
