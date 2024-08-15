from kafka.admin import KafkaAdminClient, NewTopic

# Kafka bootstrap servers
bootstrap_servers = '192.168.49.2:30003'

# Create Kafka admin client
admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)

# Define topic name and number of partitions
topic_name = "test"
num_partitions = 3  # Number of partitions for the topic

# Define replication factor
replication_factor = 3  #

new_topic = NewTopic(name=topic_name, num_partitions=num_partitions, replication_factor=replication_factor)

# Create topic(s)
admin_client.create_topics(new_topics=[new_topic])

# Close the admin client
admin_client.close()