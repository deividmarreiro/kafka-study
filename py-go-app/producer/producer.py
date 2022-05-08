import json
import random
import time
from pathlib import Path

import pandas as pd
from faker import Faker
from kafka import KafkaProducer

from product import Product
from purchase import Purchase

KAFKA_TOPIC = "purchase-topic"
KAFKA_HOST = ["localhost:9092"]

faker = Faker()

FAKE_BUYERS = [faker.name() for _ in range(1, 100)]


def create_fake_products_list():
    products = pd.read_csv(Path.joinpath(Path(__file__).parent.parent, "product_data", "sample_products.csv"), sep=";")
    list_products = [Product(name=product["product_name"], price=product["price"]) for _, product in
                     products.iterrows()]

    return list_products


FAKE_PRODUCTS = create_fake_products_list()


def create_random_purchase():
    buyer = random.choice(FAKE_BUYERS)
    product = random.choice(FAKE_PRODUCTS)
    quantity = random.randint(0, 30)
    return Purchase(quantity, product.price, buyer, product).__dict__


if __name__ == "__main__":
    print("Ctrl+c to Stop!")
    producer = KafkaProducer(bootstrap_servers=KAFKA_HOST,
                             value_serializer=lambda message: json.dumps(message).encode('utf-8'))
    while True:
        msg = create_random_purchase()
        producer.send(KAFKA_TOPIC, msg)
        print(f"Message sent to topic {KAFKA_TOPIC}, message: {msg}")
        time.sleep(2)
