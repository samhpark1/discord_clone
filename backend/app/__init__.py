from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS

socketio = SocketIO(cors_allowed_origins="*")

def create_app():
    app = Flask(__name__)
    CORS(app)
    socketio.init_app(app)

    #app.config.from_object("app.config.Config")

    from app.routes import init_routes
    from app.sockets import init_sockets
    # from app.db import init_db

    init_routes(app)
    init_sockets(socketio)
    # init_db(app)

    return app