lazy val root = project
  .in(file("."))
  .settings(
    name := "stream",
    version := "0.1.0-SNAPSHOT",
    scalaVersion := "2.13.8",

    resolvers ++= Seq(
        "confluent" at "https://packages.confluent.io/maven/",
        "Maven Central" at "https://repo1.maven.org/maven2/"
    ),

    libraryDependencies ++= Seq(
        "org.scalameta" %% "munit" % "0.7.29" % Test,
        "org.apache.beam" % "beam-sdks-java-io-kafka" % "2.54.0",
        "org.apache.kafka" % "kafka-clients" % "3.7.0",
        "org.apache.spark" % "spark-core_2.13" % "3.4.0",
        "org.apache.logging.log4j" % "log4j-core" % "2.23.1",
        "org.apache.logging.log4j" % "log4j-api" % "2.23.1"
    )
  )

assemblyMergeStrategy in assembly := {
    case PathList("META-INF", xs @ _*) => MergeStrategy.discard
    case x                             => MergeStrategy.first
}