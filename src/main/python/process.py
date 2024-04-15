import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io.kafka import ReadFromKafka

KAFKA_CONFIG = {
    "consumer_config": {"bootstrap.servers": "192.168.49.2:30003"},
    "topics": ['test']
}

pipeline_options = PipelineOptions(runner="DirectRunner")
pipeline = beam.Pipeline(options=pipeline_options)
(
        pipeline
        | "ReadData" >> ReadFromKafka(**KAFKA_CONFIG)
        | "Print" >> beam.Map(print)
)

result = pipeline.run()
