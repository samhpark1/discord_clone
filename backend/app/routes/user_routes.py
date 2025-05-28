from flask import Blueprint, jsonify

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/ping")
def ping():
    return jsonify({"msg":"pong"})