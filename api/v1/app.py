#!/usr/bin/python3
""" create an instance of Flask """
from flask import Flask, Blueprint, jsonify, make_response
from models import storage
from api.v1.views import app_views
import os
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown(exceptions):
    """ cleans up """
    storage.close()


@app.errorhandler(404)
def page_not_found(err):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == ('__main__'):
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(os.getenv('HBNB_API_PORT', '5000')))
