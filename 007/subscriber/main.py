import json
from time import sleep
from json import dumps

from kafka import KafkaConsumer


connecting=True
print("Start Process")
while connecting:
    try:
        print("Start consumer Connection")
        consumer = KafkaConsumer(bootstrap_servers=['kafka:29092'], group_id = 'group1')
        print("Connection realised")
        connecting=False
    except Exception as e: 
        print(e)
        print("Broker not connected")
        connecting=True
        sleep(5)

while True:
    try:
        print("Start receiving data")
 

        # ENVIAR DATOS AL TOPICO

        consumer.subscribe(['myTopicTest'])

        consumer.poll()

        print("Message Received")
        sleep(5)
    except Exception as e: 
        print(e)
        print("Error in the topic")
        print("Waiting")
        sleep(5)
