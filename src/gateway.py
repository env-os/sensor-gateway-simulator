import os
import paho.mqtt.client as mqtt
import sensor
import time
import json


broker_url = os.environ['BROKER_URL']
broker_port = int(os.environ['BROKER_PORT'])
topic = os.environ['TOPIC']
device_id = int(os.environ['DEVICE_ID'])
latitude = float(os.environ['LATITUDE'])
longitude = float(os.environ['LONGITUDE'])


def start():
    print_configuration()
    print("connection to broker...")
    client = connect_to_broker()
    print("connection established")
    print("SENDING DATA")
    while(True):
        time.sleep(3)
        data = read_data_from_sensor()
        json_data = convert_data_to_json(data)
        print(json_data)
        publish_data_to_broker(client, json_data)


def print_configuration():
    print("BROKER_URL = " + os.environ['BROKER_URL'])
    print("BROKER_PORT = " + os.environ['BROKER_PORT'])
    print("TOPIC = " + os.environ['TOPIC'])
    print("DEVICE_ID = " + os.environ['DEVICE_ID'])
    print("LATITUDE = " + os.environ['LATITUDE'])
    print("LONGITUDE = " + os.environ['LONGITUDE'])


def connect_to_broker():
    client = mqtt.Client()
    client.connect(host=broker_url, port=broker_port)
    return client


def read_data_from_sensor():
    return sensor.get_data()


def convert_data_to_json(data):
    data_json = json.dumps({
        "deviceId": device_id,
        "data": data,
        "sendDateTime": "05/10/2019",
        "latitude": latitude,
        "longitude": longitude,

    })
    return data_json


def publish_data_to_broker(client, data):
    client.publish(topic=topic, payload=data)


start()
