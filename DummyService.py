import json

import paho.mqtt.client as mqtt

import cv2 as cv
import numpy as np


import base64
import time
import threading


def SendVideoStream ():
    global sendingVideoStream
    global cap
    global client

    while sendingVideoStream:
        # Read Frame
        _, frame = cap.read()
        _, buffer = cv.imencode('.jpg', frame)
        # Converting into encoded bytes
        jpg_as_text = base64.b64encode(buffer)
        client.publish('videoFrame', jpg_as_text)
        time.sleep(0.25)



def on_message(cli, userdata, message):

    global sendingVideoStream
    global client

    if message.topic == 'Connect':
        print ('connected')
        client.subscribe('getValue')
        client.subscribe('writeParameters')
        client.subscribe('StartVideoStream')

    if message.topic == 'getValue':
        print ('envio valor')
        client.publish('Value', 25)
    if message.topic == 'writeParameters':
        parameters = json.loads(message.payload.decode("utf-8"))
        print (parameters)
    if message.topic == 'StartVideoStream':
        client.subscribe('StopVideoStream')
        sendingVideoStream = True
        w = threading.Thread(target=SendVideoStream)
        w.start()
    if message.topic == 'StopVideoStream':
        sendingVideoStream = False


def DummyService ():
    global cap
    global client

    broker_address ="localhost"
    broker_port = 9042
    cap = cv.VideoCapture(0)
    client = mqtt.Client(transport="websockets")
    client.on_message = on_message
    client.connect(broker_address, broker_port)
    client.subscribe('Connect')
    print ('Waiting connection')
    client.loop_forever()

if __name__ == '__main__':
    # test1.py executed as script
    # do something
    DummyService()