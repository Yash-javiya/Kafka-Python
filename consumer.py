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
