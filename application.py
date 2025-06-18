import pickle
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app=application

ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_data():
    if request.method == 'POST':
            temp = float(request.form['temp'])
            rh = float(request.form['rh'])
            ws = float(request.form['ws'])
            rain = float(request.form['rain'])
            isi = float(request.form['isi'])
            dmc = float(request.form['dmc'])
            ffmc = float(request.form['ffmc'])
            region = float(request.form['region'])
            classes = float(request.form['classes'])
            
            new_data= standard_scaler.transform([[temp, rh, ws, rain, isi, dmc, ffmc,region, classes]])
            result=ridge_model.predict(new_data)
            
            return render_template('home.html',results=result[0],)


    else:
        return render_template('home.html')
# Run the app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
