from .events import register_events

def init_sockets(socketio):
    register_events(socketio)