import json
import random

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda message: json.dumps(message).encode('utf-8'))

print("Ctrl+c to Stop!")
while True:
    producer.send('kafka-python-topic', random.randint(1, 999))
