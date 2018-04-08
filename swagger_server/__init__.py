import connexion

from swagger_server import encoder

application = connexion.App(__name__, specification_dir='./swagger/')
application.app.json_encoder = encoder.JSONEncoder
application.add_api('swagger.yaml', arguments={'title': 'Swagger Petstore'})