import requests as r

url = 'http://127.0.0.1:5000/predict'

inputs = {
    'age': 0.970798,
    'anaemia': 1.156511,
    'creatinine_phosphokinase': -0.520295,
    'diabetes': -0.861052,
    'ejection_fraction': -1.104289,
    'high_blood_pressure':-0.734621,
    'platelets': 0.051001,
    'serum_creatinine':-0.361847,
    'serum_sodium': 0.770517, 
    'sex': 0.741376,
    'smoking':  1.447444,
    'time':-0.872430
}
response = r.get(url, params=inputs)
print(f'Response: {response} args: {response.json()['prediction']})')
