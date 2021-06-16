"""
Implement a trained model on a server using Flask to allow a REST API to be used to get predictions from the model.
Author: Jamie Bamforth
"""
import pandas as pd
from flask import Flask, request, jsonify
from flask_prediction_fn import predict_fn
import os

app = Flask(__name__)



@app.route('/api_predict')
def predict_api():
    meter_id = request.args.get('meter_id') #200713
    csv_url = request.args.get('csv_url')
    weather_data_df = pd.read_csv(csv_url, index_col='captured_on_h', parse_dates=True)#str(meter_id) + '_weather_feats.csv', index_col='captured_on_h', parse_dates=True)
    timestamps, preds = predict_fn(meter_id, weather_data_df)
    print(timestamps, preds)
    output = jsonify(timestamps=timestamps, consumption=preds)
    return output



if __name__ == '__main__':
    """Import model, check it is correct model, then run Flask app locally."""
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT')))