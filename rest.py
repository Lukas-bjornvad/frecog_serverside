import werkzeug

werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask
from flask_restplus import Api, Resource, cors
from connection.connector import construct_con_str
import configparser

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = construct_con_str()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config['CORS_HEADERS'] = 'Content-Type'

api = Api(app)
ns = api.namespace("rest", description="Assignment Rest")


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


