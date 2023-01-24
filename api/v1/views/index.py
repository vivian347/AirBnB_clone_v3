#!/usr/bin/python3
""" creates route """
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify
from models import storage


classes = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
}


@app_views.route('/status', strict_slashes=False)
def status():
    """ the status """
    return jsonify({"status": "OK"})

@app_views.route('/stats', strict_slashes=False)
def stats():
    """ endpoint that retrieves no of each object """
    ret_dict = {}
    for key, val in classes.items():
        ret_dict[key] = storage.count(val)
    return jsonify(ret_dict)

#if __name__ == "__main__":
 #   pass
