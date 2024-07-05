from flask import Blueprint, jsonify, request
from sqlalchemy.exc import NoResultFound

from db import db
from models import User

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/api/users/create', methods=['POST'])
def user_create():
    try:
        data = request.get_json()
        user = User(
            username=data.get("username"),
            email=data.get("email")
        )
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User added successfully"}), 200
    except Exception as e:
        return jsonify({"error": f"error in adding user: {str(e)}"}), 400

@user_routes.route('/api/users/delete', methods=['DELETE'])
def user_delete():
    try:
        data = request.get_json()
        id = data.get("id")
        username = data.get("username")
        email = data.get("email")

        metric = [None, None]

        if id != None:
            metric[0] = "id"
            metric[1] = id
            user = db.session.execute(db.select(User).filter_by(id=id)).scalar_one()
            db.session.delete(user)
            db.session.commit()
        elif username != None:
            metric[0] = "username"
            metric[1] = username
            user = db.session.execute(db.select(User).filter_by(username=username)).scalar_one()
            db.session.delete(user)
            db.session.commit()
        elif email != None:
            metric[0] = "email"
            metric[1] = email
            user = db.session.execute(db.select(User).filter_by(email=email)).scalar_one()
            db.session.delete(user)
            db.session.commit() 
        return jsonify({"message": f"User with {metric[0]}: {metric[1]} successfully deleted"}), 200
    except NoResultFound:
        return jsonify({"error": f"No User with {metric[0]}: {metric[1]} found"})

