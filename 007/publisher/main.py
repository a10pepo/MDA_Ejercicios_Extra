from time import sleep
from json import dumps
from kafka import KafkaProducer


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

while True:
    try:
        print("Start sending data")
        # Construir el json
        producer.send('prueba', {'key': '1'})
        # ENVIAR DATOS AL TOPICO
        for i in range(10):
            m = f"hello python {i}"
            producer.send('prueba1', m)
            producer.flush()
        print("Message Sent")
        sleep(5)
    except Exception as e: 
        print(e)
        print("Error in the topic")
        print("Waiting")
        sleep(5)
