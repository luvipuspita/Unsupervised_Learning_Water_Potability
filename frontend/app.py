import streamlit as st
import requests

st.title("Aplikasi Untuk Mengecek Kualitas Air")
ph = st.number_input("ph")
Hardness = st.number_input("Hardness_mg/L")
Solids_ppm = st.number_input("Solids_ppm")
Chloramines_ppm = st.number_input("Chloramines_ppm / Spouse")
Sulfate = st.number_input("Sulfate_mg/L")
Conductivity = st.number_input("Conductivity_μS/cm")
Organic_carbon_ppm = st.number_input("Organic_carbon_ppm")
Trihalomethanes = st.number_input("Trihalomethanes_μg/L")
Turbidity_NTU = st.number_input("Turbidity_NTU")

# inference
data = {'ph' : ph,
        'Hardness_mg/L' : Hardness,
        'Solids_ppm': Solids_ppm,
        'Chloramines_ppm': Chloramines_ppm,
        'Sulfate_mg/L': Sulfate,
        'Conductivity_μS/cm': Conductivity,
        'Organic_carbon_ppm': Organic_carbon_ppm,
        'Trihalomethanes_μg/L': Trihalomethanes,
        'Turbidity_NTU': Turbidity_NTU}

URL = "http://localhost:5000/water_prediction" # sebelum push backend
# URL = "https://model-deployment-backend.herokuapp.com/titanic_prediction" # URL Heroku

# komunikasi
r = requests.post(URL, json=data)
res = r.json()
if r.status_code == 200:
    st.title(res['result']['label_name'])
else:
    st.title("YAH, ERROR")
    st.write(res['message'])