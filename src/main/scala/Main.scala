import org.apache.spark.sql.SparkSession

object EvenNumberFilter {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder()
      .appName("Even Number Filter")
      .master("local[*]") // Run Spark locally using all available CPU cores
      .getOrCreate()

    // Create input data (list of numbers)
    val inputData = List(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    val input = spark.sparkContext.parallelize(inputData).filter(lambda x: x % 2 == 0).collect()

    println(input)
    // Stop the SparkSession
    spark.stop()
  }
}