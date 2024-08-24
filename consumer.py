from confluent_kafka import Consumer, KafkaError

# Kafka configuration
conf = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "my-group",
    "auto.offset.reset": "earliest",
}

# Create Consumer instance
consumer = Consumer(conf)

# Subscribe to a topic
topic = "test-topic"
consumer.subscribe([topic])

# Poll for messages
try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break
        print(
            "Received message: "
            + msg.value().decode("utf-8")
            + " from "
            + msg.topic()
            + " ["
            + str(msg.partition())
            + "]"
        )
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
from kafka_client import KafkaConsumerClient

# Kafka consumer configuration
consumer_config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "my-group",
    "auto.offset.reset": "earliest",
}

# Create a consumer instance
consumer_client = KafkaConsumerClient(consumer_config)
consumer_client.connect()
consumer_client.subscribe(["test-topic"])

# Process received messages
try:
    while True:
        msg = consumer_client.receive_messages(timeout=1.0)
        if msg:
            print(f"Received message: {msg.value().decode('utf-8')} from {msg.topic()} [{msg.partition()}]")
except KeyboardInterrupt:
    pass
finally:
    consumer_client.close()
