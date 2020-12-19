##############################################################################################################################
# Ce chapitre traite les UDF en PySpark
# User Defined Function ou UDF permet à un utilisateur de créer sa propre fonction en python, 
# de l'enregistrer avec pyspark SQL
# et de l'utiliser sur des Dataframe ou en Spark SQL
#################################################################################################################################
# import 
from pyspark.sql import SparkSession


#Initialisation 
spark = SparkSession.builder.appName('UDF en Spark').getOrCreate()

# importer un csv en dataframe 

df = spark.read.csv ('../Data/cereal.csv')
df.show()