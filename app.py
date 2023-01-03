import numpy as np
import flask
from flask import Flask, request, jsonify, render_template, make_response
from flask_restx import Api, Resource, fields
import json
import joblib
import pickle
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)

model = pickle.load(open('disease_prediction.pkl','rb'))

f = open ('disease_details.json', "r")
disease_details = json.loads(f.read())

@api.route("/api/prediction")
class MainClass(Resource):

	def options(self):
		response = make_response()
		response.headers.add("Access-Control-Allow-Origin", "*")
		response.headers.add("Access-Control-Allow-Headers", "*")
		response.headers.add("Access-Control-Allow-Methods", "*")
		return response

	def post(self):
		try:
			formData = request.json
			find_ = False
			my_list=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
			for index, (key, value) in enumerate(formData.items()):
				if value:
					my_list[index]=1 
					find_ = True

			to_predict = np.array(my_list).reshape(1,132)
			model = joblib.load('disease_prediction.pkl')
			result = model.predict(to_predict)


			for i in disease_details:
					if i["disease"]==result[0]:
						prevention=i["prevention"]
						treatment=i["treatment"]


			response = jsonify({
				"statusCode": 200,
				"status": "Prediction made",
				"result":  "No Result",
				"prevention": "No Result",
				"treatment": "No Result"
				})			


			if find_ == True :
				response = jsonify({
				"statusCode": 200,
				"status": "Prediction made",
				"result":  str(result[0]),
				"prevention": prevention,
				"treatment": treatment
				})


			response.headers.add("Access-Control-Allow-Origin", '*')
			return response
		except Exception as error:
			return jsonify({
				"statusCode": 500,
				"status": "Could not make prediction",
				"error": str(error)
			})

if __name__ == '__main__':
    app.run()
