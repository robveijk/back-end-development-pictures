from . import app
import os
import json
from flask import jsonify, request, make_response, abort, url_for  # noqa; F401

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "data", "pictures.json")
data: list = json.load(open(json_url))

######################################################################
# RETURN HEALTH OF THE APP
######################################################################


@app.route("/health")
def health():
    return jsonify(dict(status="OK")), 200

######################################################################
# COUNT THE NUMBER OF PICTURES
######################################################################


@app.route("/count")
def count():
    """return length of data"""
    if data:
        return jsonify(length=len(data)), 200

    return {"message": "Internal server error"}, 500


######################################################################
# GET ALL PICTURES
######################################################################
@app.route("/picture", methods=["GET"])
def get_pictures():
    return make_response(jsonify(data), 200)

######################################################################
# GET A PICTURE
######################################################################
def get_picture_index(id: str) -> int | None:
    """Get the index of the picture with the given id. Returns None if not found."""
    for i, pic in enumerate(data):
        if pic.get("id") == id:
            return i
    # Not found
    return None

@app.route("/picture/<int:id>", methods=["GET"])
def get_picture_by_id(id):
    picture_index = get_picture_index(id)
    if not picture_index:
        return make_response(jsonify({"message": "Picture not found"}), 404)
    return make_response(data[picture_index]), 200


######################################################################
# CREATE A PICTURE
######################################################################
@app.route("/picture", methods=["POST"])
def create_picture():
    # Check payload: 'id' field present
    if not request.is_json or not (id := request.json.get("id")):
        return make_response({"message": "Invalid input parameter"}, 422)

    # Check payload contents
    if get_picture_index(id):
        # Yes, let's capitalize "message" here :/
        return make_response(jsonify({"Message": f"picture with id {id} already present"}), 302)

    # Add picture if payload is accepted
    data.append(request.json)
    return make_response({"id": id}, 201)


######################################################################
# UPDATE A PICTURE
######################################################################


@app.route("/picture/<int:id>", methods=["PUT"])
def update_picture(id):
    # Check payload: 'id' field present
    if not request.is_json or not (id := request.json.get("id")):
        return make_response({"message": "Invalid input parameter"}, 422)

    # Get index of the picture to update:
    if not(idx := get_picture_index(id)):
        return make_response(jsonify({"message": "picture not found"}), 404)  # So inconsistent...

    # Update the picture:
    data[idx] |= request.json
    return make_response({"id": id}, 200)


######################################################################
# DELETE A PICTURE
######################################################################
@app.route("/picture/<int:id>", methods=["DELETE"])
def delete_picture(id):
    pass
