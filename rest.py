import werkzeug
from werkzeug.datastructures import FileStorage
from werkzeug.middleware.proxy_fix import ProxyFix
werkzeug.cached_property = werkzeug.utils.cached_property

from flask import Flask, send_from_directory, jsonify
from flask_restplus import Api, Resource, cors
import configparser
import os
from pathlib import Path

from connection.connector import construct_con_str
from entities.image import Image
from entities.subject import Subject

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = construct_con_str()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config['CORS_HEADERS'] = 'Content-Type'

app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

api = Api(app, version='0.0.1', title='frecog project API', description='exam project')
upload_parser = api.parser()
upload_parser.add_argument('file', location='files',type=FileStorage, required=True)

ns = api.namespace("rest", description="Assignment Rest")


# Temporary. Change under configuration
directory =  os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "images")
    )

#api.abort(errorcode, message)

@ns.route("/")
@api.response(404, "Nothing here but us lemmings")
class ResToFrom(Resource):
    '''
    Basic testing endpoint.
    '''
    @cors.crossdomain(origin='*')
    def options(self):
        return

    @cors.crossdomain(origin='*')
    def get(self):
        '''
        [Basic response code for checking for server compliance]
        '''
        return '''
            Basic testing endpoint. 
            By seeing this, the rest service should be considered active''',
            200,
            {'Access-Control-Allow-Origin':'*'}

@ns.route('/img/dl/<string:first_name>%<string:last_name>/single/<string:filename>')
@api.response(404, 'Nothing here but us lemmings')
class ResImgReveal(Resource):
    @cors.crossdomain(origin='*')
    def get(self, first_name, last_name, filename):
        """[reveals single image for download]

        Arguments:
            first_name {string} -- [subject's first name]
            last_name {string} -- [subject's last name]
            filename {string} -- [desired image file]

        Returns:
            Image file -- [flask send from directory]
            [Integer] - [status code 200]
        """        
        return send_from_directory(f'{directory}{subject}',filename, as_attachment=True), 200

@ns.route('/img/dl/<string:first_name>%<string:last_name>/all')
@api.response(404, 'Nothing here but us lemmings')
class ResImgRevealAll(Resource):
    def get(self, first_name, last_name):
        """[download all images of a specified subject]

        Arguments:
            first_name [string] - [subject's first name]
            last_name {string} -- [subject's last name]

        Raises:

        returns

        """  
        raise NotImplementedError
        return 'Not yet implemnted', 200

@ns.route('/img/info/first/<string:first_name>')
@api.response(404, 'Nothing here but us lemmings')
class ResImgInform(Resource):
    """[provides basic information about all subjects with a given first name]

        Arguments:
            first_name {string} -- [subject's first name]

        Raises:

        returns

        """  
    def get(self, first_name):
        raise NotImplementedError
        return "Not yet implemented", 200

@ns.route('/img/info/last/<string:last_name>')
@api.response(404, 'Nothing here but us lemmings')
class ResImgInform(Resource):
    def get(self, last_name):
        """[provides basic information about all subjects with a given last name½]

        Arguments:
            last_name {string} -- [subject's last name]

        Raises:

        returns

        """  
        raise NotImplementedError
        return "Not yet implemented", 200

@ns.route('/img/info/subject/<string:first_name>%<string:last_name>')
@api.response(404, 'Nothing here but us lemmings')
class ResImgInform(Resource):
    def get(self, first_name, last_name):
        """[provides basic information about all subjects with a given first name and last name]

        Arguments:
            first_name {string} -- [subject's first name]
            last_name {string} -- [subject's last name]

        Returns:
            [string] - [statuscode 200 if successful]
            [string] - [information about said individual]

        """        
        raise NotImplementedError
        return 'Not yet implemented', 200

@ns.route('/img/<string:first_name>%<string:last_name>')
@api.response(404, 'Nothing here but us lemmings')
@api.expect(upload_parser)
class ResImgUpload(Resource):
    @cors.crossdomain(origin='*')
    def post(self, first_name, last_name, file_name):
        """[Endpoint for upload]

        Arguments:
            first_name {String} -- [subject first name]
            last_name {string} -- [subject last name]

        Returns:
            [string] -- [code 204 if succesful]
        """
        # To do:
        # Check if person with name exists.
        # If not create path in repository
        # Upload file

        uploaded_img = args['file']

        raise NotImplementedError
        return 204
