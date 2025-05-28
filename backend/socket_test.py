import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("Connected to server")
    # Send a test message to the server
    sio.emit("message", {"hello": "from client"})

@sio.event
def disconnect():
    sio.emit("message", {"bye bye": "from client"})
    print("Disconnected from server")

@sio.on("message")
def on_message(data):
    print("Message received from server:", data)

# Connect to your Flask-SocketIO server URL (adjust port if needed)
sio.connect('http://127.0.0.1:5000')

# Keep the client running to listen for events
sio.wait()
