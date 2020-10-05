from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from flask_cors import CORS, cross_origin
from json import dumps

from WebScraping.news import news
from WebScraping.sports import sports
from WebScraping.politics import politics
from WebScraping.health import health
from WebScraping.tech import tech

app = Flask(__name__)
api = Api(app)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

class News(Resource):
    def get(self):
        return news()

class Sports(Resource):
    def get(self):
        return jsonify(sports())

class Politics(Resource):
    def get(self):
        return jsonify(politics())

class Health(Resource):
    def get(self):
        return jsonify(health())

class Tech(Resource):
    def get(self):
        return jsonify(tech())

api.add_resource(News, '/news') 
api.add_resource(Sports, '/sports') 
api.add_resource(Politics, '/politics') 
api.add_resource(Health, '/health') 
api.add_resource(Tech, '/tech') 


if __name__ == '__main__': 
    app.run()