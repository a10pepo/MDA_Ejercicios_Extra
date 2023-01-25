from pyspark.sql import SparkSession

# Import sql functions
from pyspark.sql.functions import *

from pyspark.sql.types import StructType, StructField, StringType


def init_spark():
    print("Creating session")   
    spark = SparkSession.builder.appName("EDEM_APP").getOrCreate()
    return spark




def main():
    spark=init_spark()

    schema = StructType([ 
    StructField("sale_id", StringType(), True),
    StructField("amount" , StringType(), True),
    StructField("date_sale" , StringType(), True),
    StructField("product_id" , StringType(), True),
    StructField("user_id" , StringType(), True),
    StructField("store_id" , StringType(), True), 
    ])

    # stream_detail_df = spark.readStream.format("kafka")\
    #                  .option("kafka.bootstrap.servers", "kafka:29092")\
    #                  .option("subscribe", "sale")\
    #                  .option("startingOffsets", "earliest")\
    #                  .load() \
    #                  .select(from_json(col("value").cast("string"), schema).alias("parsed_value")) \
    #                  .select(col("parsed_value.*"))
     
    # df = stream_detail_df.select('*')
  
    # # Start running the query that prints the running counts to the console
    # query = df\
    #     .writeStream\
    #     .outputMode('Append')\
    #     .format('console')\
    #     .start()

    # query.awaitTermination()

    spark.sql("set spark.sql.streaming.schemaInference=true")

   

    list_topics = "product,users,status_name,country,city,store,sale,order_status"

    df_json = spark.readStream.format("kafka")\
                    .option("kafka.bootstrap.servers", "kafka:29092")\
                    .option("subscribe", list_topics)\
                    .option("startingOffsets", "earliest")\
                    .option("includeHeaders","true")\
                    .option("inferSchema", "true")\
                    .load() \
                    .withColumn("value", regexp_replace(col("value").cast("string"), "\\\\", "")) \
                    .withColumn("value", regexp_replace(col("value"), "^\"|\"$", "")) \
                    


    print(df_json)

    # df = df_json.selectExpr("CAST(topic AS STRING)", "CAST(partition AS STRING)", "CAST(offset AS STRING)", "CAST(value AS STRING)")
    
    df = df_json.selectExpr("CAST(topic AS STRING)", "CAST(value AS STRING)")

    # df_json.select(from_json(col("data"), schema).alias("data"))\
    #   .writeStream\
    #   .format("console")\
    #   .outputMode("append")\
    #   .start()\
    #   .awaitTermination()

    query = df.writeStream.format("console").option("truncate", "False").start()
    
    query.awaitTermination()

if __name__ == '__main__':
  main()

