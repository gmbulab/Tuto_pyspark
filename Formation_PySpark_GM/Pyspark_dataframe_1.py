# Initialisation 
from pyspark.sql import SparkSession
spark =SparkSession.builder.appName('Dataframe niv 1').getOrCreate()

# import df 
df = spark.read.json('..\\..\\..\\Data_formation\\people.json')

# print schemas 
print(df.printSchema())
# Les  data dans le df 
print(df.show())

# Les columns 
print(df.columns)

# L'équivalent de shape en Pandas  
print(df.count(), len(df.columns))

# Gérer les types avec StructType et StructField
from pyspark.sql.types import StructField, StructType, IntegerType, StringType
data_schema = [StructField("age", IntegerType(), True), StructField("name", StringType(), True)]
fin_sch = StructType(data_schema)

# Creer une colonne avec withColumn
df = df.withColumn('dou_age', df['age']*2)
# renommer une colonne avec withColumnRenamed
df = df.withColumnRenamed('name', 'nom')

print('ok')