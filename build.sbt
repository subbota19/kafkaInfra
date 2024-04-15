val scala3Version = "3.4.0"

lazy val root = project
  .in(file("."))
  .settings(
    name := "stream",
    version := "0.1.0-SNAPSHOT",

    scalaVersion := scala3Version,

    // search for dependencies in the Confluent Maven repository
    resolvers += "confluent" at "https://packages.confluent.io/maven/",

    libraryDependencies ++= Seq(
        ("org.scalameta" %% "munit" % "0.7.29" % Test),
        ("org.apache.beam" % "beam-sdks-java-io-kafka" % "2.54.0"),
        ("org.apache.kafka" % "kafka-clients" % "3.7.0")
    )
  )
