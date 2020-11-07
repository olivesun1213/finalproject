# Dependencies Setup

import pandas as pd
from flask import Flask, request, redirect, url_for, flash, jsonify, render_template
import numpy as np
import pickle as p
import json
import tensorflow as tf
import keras
from keras.models import load_model

# Create an instance of the Flask class
app = Flask(__name__)

model = load_model('Models/mdl-neuralnetwork.h5')

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/predict', methods=["GET","POST"])
def predict(user_features):

    final_features = [np.array(user_features)]
    prediction = model.predict(final_features)
    
    # return a response in json format 
    return render_template('prediction.html', prediction_text=prediction)