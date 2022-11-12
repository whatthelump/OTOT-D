# Adapted from https://docs.confluent.io/kafka-clients/python/current/overview.html#ak-producer

from confluent_kafka import Producer
import socket

conf = {'bootstrap.servers': "localhost:29092,localhost:39092,localhost:49092",
        'client.id': socket.gethostname()}

producer = Producer(conf)

if __name__ == "__main__":
    inputstr = ""
    print("Producer: ")
    while inputstr != "quit":
        inputstr = input('>')
        producer.produce("taskd", key = "key", value = inputstr)

    producer.flush()