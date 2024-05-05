import asyncio
from aiokafka import AIOKafkaProducer


class KafkaProducer:
    def __init__(self, bootstrap_servers):
        self.bootstrap_servers = bootstrap_servers
        self.producer = None

    async def connect(self):
        self.producer = AIOKafkaProducer(bootstrap_servers=self.bootstrap_servers)
        await self.producer.start()

    async def send_message(self, topic, message):
        await self.producer.send_and_wait(topic, message.encode('utf-8'))

    async def disconnect(self):
        await self.producer.stop()


async def main():
    kafka_bootstrap_servers = '192.168.49.2:30003'
    kafka_topic = 'test'

    producer = KafkaProducer(bootstrap_servers=kafka_bootstrap_servers)
    await producer.connect()

    try:
        # Sending a test message
        await producer.send_message(kafka_topic, 'Hello, Kafka!')
    except KeyboardInterrupt:
        pass
    finally:
        # Close the producer
        await producer.disconnect()


if __name__ == '__main__':
    asyncio.run(main())