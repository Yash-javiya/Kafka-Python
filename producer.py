from kafka_client import KafkaProducerClient

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Kafka producer configuration
producer_config = {
    "bootstrap.servers": "localhost:9092"
}

# Create a producer instance
producer_client = KafkaProducerClient(producer_config)
producer_client.connect()

# Send messages
topic = "test-topic"
for i in range(10):
    message = f"Message {i}"
    producer_client.send_message(topic, message, callback=delivery_report)

# Wait for message processing
producer_client.wait_for_processing()
