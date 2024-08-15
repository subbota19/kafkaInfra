package com.stream

import org.apache.spark.{SparkConf, SparkContext}

object EvenNumberFilter {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf()
      .setAppName("Sum of Numbers")
      .setMaster("local[*]")

    val sc = new SparkContext(conf)
    val inputData = List(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    sc.parallelize(inputData).filter(_ % 2 == 0).collect().foreach(println)
    sc.stop()
  }
}