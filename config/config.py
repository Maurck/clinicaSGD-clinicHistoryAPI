'''
config.py: modulo donde se configura la aplicación
'''
import os
from dotenv import load_dotenv
from flask import Flask
from flask_lambda import FlaskLambda
from flask_cors import CORS
from mongoengine import connect

def server_config(app):
    load_dotenv()
    cors_config(app)
    database_config()

def cors_config(app):
    CORS(app=app, send_wildcard=True)

def database_config():
    DB_URI = os.getenv('DB_URI')
    connect(host=DB_URI)

def get_app(__name__):

    server_status = os.getenv('SERVER_STATUS', 'DEVELOPMENT')

    if server_status == 'DEVELOPMENT':
        app = Flask(__name__)
    elif server_status == 'PRODUCTION':
        app = FlaskLambda(__name__)

    return app

def run_app(app):
    server_status = os.getenv('SERVER_STATUS', 'DEVELOPMENT')

    if server_status == 'DEVELOPMENT':
        app.run(debug=True, host='0.0.0.0', port=5000)
    elif server_status == 'PRODUCTION':
        app.run(debug=True)
    
