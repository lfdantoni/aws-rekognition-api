#!/usr/bin/env python3

# import connexion

# from swagger_server import encoder
# # from flask import Flask

# # application = Flask(__name__)
# # app = application

# # @app.route("/")     
# # def hello():         
# # 	return "Hello World!"

# application = connexion.App(__name__, specification_dir='./swagger/')
# application.app.json_encoder = encoder.JSONEncoder
# application.add_api('swagger.yaml', arguments={'title': 'Swagger Petstore'})

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Swagger Petstore'})
    return app

if __name__ == '__main__':
    application.run(port=8080)
