from time import sleep
from json import dumps
from kafka import KafkaProducer
import requests

connecting=True
print("Starting connection")

# Tries to connect to kafka broker until connected

while connecting:
    try:
        print("Start producer Connection")
        producer = KafkaProducer(bootstrap_servers=['kafka:29092'],value_serializer=lambda x: dumps(x).encode('utf-8'))
        print("Connection realised")
        connecting=False
    except Exception as e: 
        print(e)
        print("Broker not connected")
        connecting=True
        sleep(5)

# Start sending data 
 
while True:
    try:
        for i in range (0,100):
            
            # Get request from demo API. Recieving a json for each product.
            r = requests.get("https://dummyjson.com/products?skip="+str(i)+"&limit=1")
            res = r.json()
            message = res['products'][0]
            # Send json with product data to kafka topic 'topic_test'
            producer.send("topic_test",message)
            producer.flush()
            print("Message Sent")

    except Exception as e: 
        print(e)
        print("Error in the topic")
        print("Waiting")
        sleep(5)
