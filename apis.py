from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS  # Import CORS
import requests

headers = {"Authorization": "Bearer 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"}

app = Flask(__name__)
api = Api(app)
CORS(app, resources={r"/": {"origins": "*"}})


class T5_small(Resource):
    @staticmethod
    def post():
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        payload = request.get_json()
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()


class qna(Resource):
    @staticmethod
    def post():
        API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
        payload = request.get_json()
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()


class translate(Resource):
    @staticmethod
    def post():
        API_URL = "https://api-inference.huggingface.co/models/facebook/mbart-large-50-many-to-many-mmt"
        payload = request.get_json()
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()


class text_generation(Resource):
    @staticmethod
    def post():
        API_URL = "https://api-inference.huggingface.co/models/gpt2"
        payload = request.get_json()
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()


api.add_resource(T5_small, '/summarize')
api.add_resource(qna, '/qna')
api.add_resource(translate, '/translate')
api.add_resource(text_generation, '/text_generation')

if __name__ == '__main__':
    app.run(debug=False)
