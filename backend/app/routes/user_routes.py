from flask import Blueprint, jsonify, request
from app.db import db_manager
from app.tables.user import User

user_routes = Blueprint("user_routes", __name__)

user_routes = Blueprint("user_routes", __name__)

@user_routes.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    try:
        with db_manager.sql.session_scope() as session:
            user = User(
                username=data['username'],
                email=data['email'],
                hashed_password=data['hash']
            )
            session.add(user)
            # No need to commit — handled by session_scope
        return jsonify({'message': 'User created'}), 201

    except Exception as e:
        print("❌ Error during user creation:", e)
        return jsonify({'error': str(e)}), 500
