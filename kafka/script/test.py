from confluent_kafka import Producer

# Kafka broker details
bootstrap_servers = '192.168.49.2:30003'  # Replace with your Kafka broker host
topic = 'yyy'  # Replace with your Kafka topic

# Kafka producer configuration
conf = {
    'bootstrap.servers': bootstrap_servers,
}

# Create Kafka producer
producer = Producer(**conf)

# Produce a message
try:
    producer.produce(topic, key=None, value='Test message from Kafka producer')
    producer.flush()  # Wait for messages to be delivered
    print("Message sent successfully!")
except Exception as e:
    print(f"Failed to send message: {e}")
