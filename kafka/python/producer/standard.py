from confluent_kafka import Producer


class KafkaProducer:
    def __init__(self, bootstrap_servers):
        self.bootstrap_servers = bootstrap_servers
        self.producer = Producer({'bootstrap.servers': self.bootstrap_servers})

    def send_message(self, topic, message):
        # Asynchronously produce a message, delivery report callback is specified
        def delivery_report(err, msg):
            if err is not None:
                print(f'Message delivery failed: {err}')
            else:
                print(f'Message delivered to topic {msg.topic()} partition {msg.partition()}')

        # Produce message to topic
        self.producer.produce(topic, message.encode('utf-8'), callback=delivery_report)

        # Wait up to 1 second for events. Callbacks will be invoked during
        # this method call if the message is acknowledged.
        self.producer.poll(1)

    def close(self):
        # Flush all messages and close the producer
        self.producer.flush()


if __name__ == '__main__':
    # Example usage
    kafka_bootstrap_servers = '192.168.49.2:30092'
    kafka_topic = 'fff'

    producer = KafkaProducer(bootstrap_servers=kafka_bootstrap_servers)

    try:
        # Sending a test message
        producer.send_message(kafka_topic, 'Yauheni on the line!')
    except KeyboardInterrupt:
        pass
    finally:
        # Close the producer
        producer.close()