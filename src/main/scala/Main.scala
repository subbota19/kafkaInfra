import org.apache.beam.sdk.Pipeline
import org.apache.beam.sdk.io.kafka.{KafkaIO, KafkaRecord}
import org.apache.kafka.common.serialization.StringDeserializer

object KafkaReader {
  def main(args: Array[String]): Unit = {
    val pipeline = Pipeline.create()

    val bootstrapServers = "localhost:9092"
    val topic = "test"
    val groupId = "your-group-id"

    val kafkaConfig = KafkaIO.read[String, String]()
      .withBootstrapServers(bootstrapServers)
      .withTopics(Seq(topic))
      .withConsumerConfigUpdates(Map("group.id" -> groupId))
      .withKeyDeserializer(classOf[StringDeserializer])
      .withValueDeserializer(classOf[StringDeserializer])

    val messages = pipeline.apply(KafkaIO.read[String, String]().withBootstrapServers(bootstrapServers)
      .withTopics(Seq(topic))
      .withKeyDeserializer(classOf[StringDeserializer])
      .withValueDeserializer(classOf[StringDeserializer])
      .withoutMetadata())

    messages
      .map(record => record.getKV.getKey + ": " + record.getKV.getValue)
      .map(println)

    pipeline.run().waitUntilFinish()
  }
}