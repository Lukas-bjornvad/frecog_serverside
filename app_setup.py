import werkzeug
from werkzeug.middleware.proxy_fix import ProxyFix

werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask, send_from_directory
from flask_restplus import Api, cors
from flask_sqlalchemy import SQLAlchemy
from connection.connector import construct_con_str
from settings.pathing import os_parse_path


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = construct_con_str()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['CORS_HEADERS'] = 'Content-Type'
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

db = SQLAlchemy(app)
api = Api(app)



