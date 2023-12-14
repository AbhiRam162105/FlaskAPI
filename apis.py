
from flask import Flask, jsonify, request 
from flask_restful import Resource, Api 
from flask_cors import CORS  # Import CORS
import requests

# creating the flask app 
app = Flask(__name__) 
# creating an API object 
api = Api(app) 
CORS(app, resources={r"/*": {"origins": "*"}})  
# making a class for a particular resource 
# the get, post methods correspond to get and post requests 
# they are automatically mapped by flask_restful. 
# other methods include put, delete, etc. 
''' 
"inputs": "content"
'''
class T5_small(Resource):
   def post(self):  
    API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {"Authorization": "Bearer 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"}
    payload = request.get_json()
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


''' 
"inputs": {
	"question": "What is my name?",
	"context": "My name is Clara and I live in Berkeley."
  },
'''
class qna(Resource):
  def post(self):    
    API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
    headers = {"Authorization": "Bearer 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"}
    payload = request.get_json()
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

''' 
{
    "inputs": "My name is Sarah Jessica Parker but you can call me Jessica", "parameters": {"src_lang": "en_XX", "tgt_lang": "fr_XX"}
}
'''
class translate(Resource):
   def post(self):    
    API_URL = "https://api-inference.huggingface.co/models/facebook/mbart-large-50-many-to-many-mmt"
    headers = {"Authorization": "Bearer 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"}
    payload = request.get_json()
    response = requests.post(API_URL, headers=headers, json=payload)
    print(response)
    return response.json()

# adding the defined resources along with their corresponding urls 
api.add_resource(T5_small, '/summarize') 
api.add_resource(qna, '/qna')
api.add_resource(translate, '/translate')

# driver function 
if __name__ == '__main__': 
  
    app.run(debug = False) 