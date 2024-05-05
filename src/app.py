from datetime import datetime
from multiprocessing import Pool
from producer.kafka import CustomProducer

from random import randint
from json import dumps


def runner(bootstrap_servers, topic, process_id):
    producer = CustomProducer(bootstrap_servers)
    for _ in range(100):
        message = {
            "id": randint(0, 100),
            "type": "multiprocessing",
            "message": "TEST MESSAGE",
            "datetime": str(datetime.now().isoformat()),
            "process_id": process_id
        }
        producer.send_message(topic, dumps(message))

    producer.close()


def main():
    kafka_bootstrap_servers = '192.168.49.2:30003'
    kafka_topic = 'test'
    num_procs = 4
    pool = Pool(num_procs)

    dt = datetime.now()

    for _ in range(num_procs):
        pool.apply_async(runner, kwds={
            "bootstrap_servers": kafka_bootstrap_servers,
            "topic": kafka_topic,
            "process_id": _
        })
    pool.close()
    pool.join()

    print(datetime.now() - dt)


if __name__ == '__main__':
    main()
