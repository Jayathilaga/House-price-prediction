import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('Random_forest_regressor_model.pkl', 'rb'))
 
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/predict',methods=['POST'])
def predict():
    new = pd.DataFrame(request.form.values()).T
    new.columns = ['ml_num', 'property_type', 'br', 'br_plus', 'br_final', 'bath_tot',
       'taxes', 'lp_dol', 'yr_built', 'gar_type', 'garage',
       'topHighschoolScore', 'topBelowHighschoolScore', 'geo_latitude',
       'geo_longitude', 'lot_frontfeet', 'lot_depthfeet', 
       'sqft_numeric', 'id_community', 'id_municipality', 'lot_size','date_start',
       'date_end']
    new['date_start'] = pd.to_datetime(new['date_start'], format='%Y-%m-%d %H:%M:%S')
    new['date_end'] = pd.to_datetime(new['date_end'], format='%Y-%m-%d %H:%M:%S')
    new['diff_in_dates'] =pd.to_numeric(new['date_end']-  new ['date_start'])
    new['id_municipality'] =new['id_municipality'].astype(object)
    new['id_community'] = new['id_community'].astype(object)
    prediction = model.predict(new)
 
    output = prediction[0]
 
    return render_template('index.html', prediction_text='Predicted House Price is {}'.format(output))
 
 
if __name__ == "__main__":
    app.run(debug=True)