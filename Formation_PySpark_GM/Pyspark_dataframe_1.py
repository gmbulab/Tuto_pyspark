# Initialisation 
from pyspark.sql import SparkSession
spark =SparkSession.builder.appName('Dataframe niv 1').getOrCreate()

print('ok')