import numpy as np
import pickle as p
from flask import Flask
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser

app = Flask('My Backend')
api = Api(app)

feature_names = ['age', 'anaemia', 'creatinine_phosphokinase', 'diabetes',
                'ejection_fraction', 'high_blood_pressure', 'platelets',
                'serum_creatinine', 'serum_sodium', 'sex', 'smoking', 'time']

class GetPrediction(Resource):
    def __init__(self):
        with (open('rf1.pickle', 'rb') as f):
            self.model = p.load(f)
        self.reqparser = RequestParser()
        for name in feature_names:
            self.reqparser.add_argument(name, required=True, location='args')

    def get(self):
        args = self.reqparser.parse_args()
        inputs = np.array([[args[name] for name in feature_names]])
        # print(args)
        return {'prediction':int(self.model.predict(inputs)[0])}

api.add_resource(GetPrediction, '/predict')

if __name__ == '__main__':
    app.run(debug=True)