from confluent_kafka import Producer


class CustomProducer:
    def __init__(self, bootstrap_servers):
        self.producer = Producer({'bootstrap.servers': bootstrap_servers})

    def send_message(self, topic, message):
        # Asynchronously produce a message, delivery report callback is specified
        # def delivery_report(err, msg):
        #     if err is not None:
        #         print(f'Message delivery failed: {err}')
        #     else:
        #         print(f'Message delivered to topic {msg.topic()} partition {msg.partition()}')

        # Produce message to topic
        self.producer.produce(topic, message.encode('utf-8'))

        self.producer.poll(1)

    def close(self):
        # Flush all messages and close the producer
        self.producer.flush()
