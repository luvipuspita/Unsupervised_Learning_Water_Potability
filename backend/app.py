from crypt import methods
from pyexpat import model
from unittest import result
from urllib import response
from flask import Flask, request, jsonify
import pickle
import pandas as pd
import requests
from sqlalchemy import column

# inisiasi
app = Flask(__name__)


# open model
def open_model(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model

model_water = open_model("pipe_water.pkl")

# fungsi untuk inference water
def inference_water(data, model):
    """
    input
    """
    
    LABEL=[0, 1]
    columns = ['ph', 'Hardness_mg/L', 'Solids_ppm', 'Chloramines_ppm', 'Sulfate_mg/L', 'Conductivity_μS/cm', 'Organic_carbon_ppm', 'Trihalomethanes_μg/L', 'Turbidity_NTU']
    data = pd.DataFrame([data], columns=columns)
    res = model.predict(data)
    return res[0], LABEL[res[0]]

# halaman home
@app.route("/")
def homepage():
    return "<h1> Deployment Model Backend </h1>"

# halaman inference water
@app.route('/water_prediction', methods=['POST'])
def water_predict():
    """
    content = 
    {
        'ph' : xx,
        'Hardness_mg/L' : xx,
        'Solids_ppm': xx,
        'Chloramines_ppm': xx,
        'Sulfate_mg/L': xx,
        'Conductivity_μS/cm': xx,
        'Organic_carbon_ppm': xx,
        'Trihalomethanes_μg/L': xx,
        'Turbidity_NTU': xx
    }
    """
    columns = ['ph', 'Hardness_mg/L', 'Solids_ppm', 'Chloramines_ppm', 'Sulfate_mg/L', 'Conductivity_μS/cm', 'Organic_carbon_ppm', 'Trihalomethanes_μg/L', 'Turbidity_NTU']
    content = request.json
    newdata = [
        content['ph'],
        content['Hardness_mg/L'],
        content['Solids_ppm'],
        content['Chloramines_ppm'],
        content['Sulfate_mg/L'],
        content['Conductivity_μS/cm'],
        content['Organic_carbon_ppm'],
        content['Trihalomethanes_μg/L'],
        content['Turbidity_NTU']
                ]
    # newdata = pd.DataFrame([newdata], columns=columns)

    res_idx, res_label = inference_water(newdata, model_water)
    result = {
        'label_idx': str(res_idx),
        'label_name': res_label
    }
    
    response = jsonify(success=True,
                        result=result)
    return response, 200

# run app di local
# jika deploy di heroku, comment baris dibawah ini
app.run(debug=True)