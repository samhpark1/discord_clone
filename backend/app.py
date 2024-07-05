from flask import Flask, request, redirect, jsonify
from flask_cors import CORS

from config import Config
from db import db
from models import User
from routes import user_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    db.init_app(app)

    app.register_blueprint(user_routes)

    return app

   

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)