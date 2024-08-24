from confluent_kafka import Producer, Consumer, KafkaError

class KafkaClientBase:
    def __init__(self, config):
        self.config = config
        self.client = None

    def connect(self):
        """This method will be overridden in the producer and consumer classes."""
        pass

    def wait_for_processing(self):
        """Waits for any outstanding messages to be processed."""
        if isinstance(self.client, Producer):
            self.client.flush()

    def close(self):
        """Close the client connection."""
        if isinstance(self.client, Consumer):
            self.client.close()

class KafkaProducerClient(KafkaClientBase):
    def connect(self):
        """Initialize the Kafka producer."""
        self.client = Producer(self.config)

    def send_message(self, topic, message, callback=None):
        """Produce a message to the Kafka topic."""
        if not self.client:
            raise Exception("Producer is not connected. Call connect() before sending messages.")
        
        self.client.produce(topic, message.encode('utf-8'), callback=callback)
        self.client.poll(0)  # Poll to handle delivery reports if a callback is provided

class KafkaConsumerClient(KafkaClientBase):
    def connect(self):
        """Initialize the Kafka consumer."""
        self.client = Consumer(self.config)
    
    def subscribe(self, topics):
        """Subscribe to a list of topics."""
        self.client.subscribe(topics)
    
    def receive_messages(self, timeout=1.0):
        """Poll for messages from the Kafka topic."""
        if not self.client:
            raise Exception("Consumer is not connected. Call connect() before receiving messages.")
        
        msg = self.client.poll(timeout)
        if msg is None:
            return None
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                return None
            else:
                raise KafkaError(msg.error())
        
        return msg
