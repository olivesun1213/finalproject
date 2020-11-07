# Dependencies Setup

import pandas as pd
from flask import Flask, request, redirect, url_for, flash, jsonify, render_template
import requests
import numpy as np
import pickle as p
import json
import tensorflow as tf
import keras
from keras.models import load_model

# Create an instance of the Flask class
app = Flask(__name__)

#model = load_model('Models/mdl-neuralnetwork.h5')

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/predict', methods=["GET", "POST"])
def predict():
    if request.method == "POST": 
        # getting input with name = hour in HTML form 
        #hourURL = request.form["hour"]
        #hour = requests.get(hourURL)
        # getting input with name = road_class in HTML form  
        #road_class = request.form.get("road_class") 
        data = request.form
        for key in data:
            print ('form key '+key+" "+data[key])

        #print(data) 
        #print(hourURL)
        #print(road_class)
        #return "Data: "+hour + road_class 

    data = [[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    prediction = model.predict(data)
    #prediction = np.array2string(model.predict(data))
    print(prediction)
    #return jsonify(prediction)

# # function to one hot encode user input for model prediction
# def onehot_encode(feature, value):
#     hour_array = []
#     if 
#     switch (feature):
#         case "hour":



if __name__ == '__main__':
    #modelfile = 'models/final_prediction.pickle'
    modelfile = 'models/DecisionTree_final_model.pickle'
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=True, host='0.0.0.0')