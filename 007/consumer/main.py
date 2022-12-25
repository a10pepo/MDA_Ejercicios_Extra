from kafka import KafkaConsumer
from json import loads
from time import sleep



connecting=True
print("Start Process")
while connecting:
    try:
        print("Start producer Connection")
        consumer = KafkaConsumer('prueba',
                                bootstrap_servers=['kafka:29092'],
                                group_id='my-group',
                                auto_offset_reset='earliest',
                                enable_auto_commit=True,
                                value_deserializer=lambda x: loads(x.decode('utf-8')))
        for msg in consumer:
            print (msg)       
        print("Connection realised")
        connecting=False
    except Exception as e: 
        print(e)
        print("Broker not connected")
        connecting=True
        sleep(1)



