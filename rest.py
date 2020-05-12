import werkzeug
from werkzeug.middleware.proxy_fix import ProxyFix

werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask, send_from_directory
from flask_restplus import Api, Resource, cors
from connection.connector import construct_con_str
import configparser
import os
from settings.pathing import os_parse_path

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = construct_con_str()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config['CORS_HEADERS'] = 'Content-Type'

app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

api = Api(app)
ns = api.namespace("rest", description="Assignment Rest")

# Temporary. Change under configuration
directory =  os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "images")
    )
print(directory)


@ns.route("/")
@api.response(404, "Nothing here but us lemmings")
class ResToFrom(Resource):
    @cors.crossdomain(origin='*')
    def options(self):
        return

    @cors.crossdomain(origin='*')
    def get(self):
        return 'boop', 200, {'Access-Control-Allow-Origin':'*'}

    def post(self):
        return None, 201

@ns.route('/<string:filename>')
@api.response(404, 'Nothing here but us lemmings')
class ResImg(Resource):
    @cors.crossdomain(origin='*')
    def get(self, filename):
        return send_from_directory(directory,filename)
