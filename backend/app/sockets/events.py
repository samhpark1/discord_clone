def register_events(socketio):

    @socketio.on("connect")
    def handle_connect():
        print("Client connected")

    @socketio.on("message")
    def handle_message(data):
        print(f"Received: {data}")
        socketio.send("Message received")