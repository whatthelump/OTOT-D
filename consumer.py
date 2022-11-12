# Adapted from https://docs.confluent.io/kafka-clients/python/current/overview.html#ak-consumer

from confluent_kafka import Consumer

conf = {'bootstrap.servers': "localhost:29092,localhost:39092,localhost:49092",
        'group.id': "taskd",
        'auto.offset.reset': 'smallest'}

consumer = Consumer(conf)
consumer.subscribe(["taskd"])

if __name__ == "__main__":
    print("Consumer: ")
    while True:
        message = consumer.poll(timeout = 1.0)
        if message is None:
            continue
        else:
            print(message.value().decode('utf-8'))

    consumer.close()