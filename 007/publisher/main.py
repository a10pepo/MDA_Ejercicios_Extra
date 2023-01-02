from time import sleep
from json import dumps
from kafka import KafkaProducer

def create_producer():
    connecting=True
    print("Start Process")
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
    return producer

def send_data(producer):
    while True:
        try:
            print("Start sending data")
            # Construir el json
            # ENVIAR DATOS AL TOPICO
            producer.flush()
            print("Message Sent")
            sleep(5)
        except Exception as e: 
            print(e)
            print("Error in the topic")
            print("Waiting")
            sleep(5)

if __name__ == '__main__':
    producer = create_producer()
    send_data(producer)
