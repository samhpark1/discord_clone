from flask import Blueprint, jsonify, request
from datetime import datetime
from app.db import db_manager
from app.models import UserModel

user_routes = Blueprint("user_routes", __name__)

@user_routes.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()

        username = data["username"]
        email = data["email"]
        avatar = data["avatar"]
        password_hash = data["password_hash"]
        created_at = datetime.fromisoformat(data["created_at"])

        created_username = UserModel.create_user(
            username=username,
            email=email,
            avatar=avatar,
            password_hash=password_hash,
            created_at=created_at
        )

        return jsonify({"msg": f"{created_username} created successfully!"}), 201

    except KeyError as e:
        return jsonify({"err": f"Missing field in request body: {str(e)}"}), 400
    except ValueError as e:
        return jsonify({"err": f"Invalid datetime format: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"err": f"Unexpected error: {str(e)}"}), 500


    
