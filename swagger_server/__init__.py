import connexion

from swagger_server import encoder
# from flask import Flask

# application = Flask(__name__)
# app = application

# @app.route("/")     
# def hello():         
# 	return "Hello World!"

application = connexion.App(__name__, specification_dir='./swagger/')
application.app.json_encoder = encoder.JSONEncoder
application.add_api('swagger.yaml', arguments={'title': 'Swagger Petstore'})