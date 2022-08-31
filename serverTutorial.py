import time
import threading

from flask import Flask
from flask_socketio import SocketIO
app = Flask(__name__)

socketio = SocketIO (app, cors_allowed_origins="*")


@socketio.on ('connectPlatform')
def handle_message():
    global socketio
    print ('connect')
    connectMsg = input('Input messsage on connection')
    socketio.emit('connected', connectMsg)


if __name__ == '__main__':
    print ('Starting server')

    # start listening
    socketio.run(app, port=5000)