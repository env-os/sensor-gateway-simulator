import paho.mqtt.client as mqtt #import the client1
import sys
import sensor
import time
import json

def execute(addres):
    broker_address=addres 
    client = mqtt.Client("P1") #create new instance
    client.connect(broker_address) #connect to broker
    while(True):
        data = elaborate_data(read_data())
        send_data(client, data)

def read_data():
    return sensor.generate_data()

def elaborate_data(data):
    time.sleep(5)
    mqtt_msg = json.dumps({"data": data, "device":  "Sensore fumo"});
    print(mqtt_msg)
    return mqtt_msg

def send_data(client, data):
    client.publish(sys.argv[2],data)

execute(sys.argv[1])
