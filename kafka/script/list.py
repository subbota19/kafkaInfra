from confluent_kafka.admin import AdminClient


def list_kafka_topics(bootstrap_servers):
    # Create an AdminClient instance
    admin_client = AdminClient({'bootstrap.servers': bootstrap_servers})

    # Get the list of topics
    topics_metadata = admin_client.list_topics(timeout=10)

    # Extract topic names from the metadata
    topic_names = [topic for topic in topics_metadata.topics]

    return topic_names


# Example usage
bootstrap_servers = '192.168.49.2:30003' # Change to your Kafka bootstrap servers
topics = list_kafka_topics(bootstrap_servers)
print("List of topics:", topics)
