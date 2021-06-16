"""
Request preditCions from the model as a client would and test teh output
Author: Jamie Bamforth
"""
import requests


def check_responses():
    """Take test features and actual predictions for these features and feed them to the model through the API. Check
    the predictions from the API match the actual predictions and print 'Success!' if so, else print 'Failure :('"""
    response_preds = []
    payload = {'meter_id':200713,
               'csv_url':'https://raw.githubusercontent.com/Jamie-B22/ITC_final_project/3c6ca44c2db3c56c8de12f46f80a2c5f66baadb6/CP4/200713_weather_feats.csv'}
    response_preds.append(requests.get('https://power-ranges.herokuapp.com/api_predict', params=payload).text)
    print(response_preds)


if __name__ == '__main__':
    """Import data to feed the model and check the responses from the model API match the actual predictions."""
    check_responses()