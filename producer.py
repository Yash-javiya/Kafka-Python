from confluent_kafka import Producer

# Kafka configuration
conf = {"bootstrap.servers": "localhost:9092"}

# Create Producer instance
producer = Producer(conf)


# Callback for delivery reports
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")


# Produce a message
topic = "test-topic"
for i in range(10):
    message = f"Message {i}"
    producer.produce(topic, message.encode("utf-8"), callback=delivery_report)

# Wait for any outstanding messages to be delivered and delivery report
producer.flush()
