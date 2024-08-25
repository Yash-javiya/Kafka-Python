from kafka_client import KafkaConsumerClient

# Kafka consumer configuration
consumer_config = {
    "bootstrap.servers": "localhost:29092,localhost:29094,localhost:29096",
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
