##############################################################################################################################
# Ce chapitre traite les UDF en PySpark. 
# Les UDF sont très utiles en Spark SQL
# User Defined Function ou UDF permet à un utilisateur de créer sa propre fonction en python, 
# de l'enregistrer avec spark SQL et de l'utiliser sur des Dataframe ou en Spark SQL grâce  à udf()
# Par exemple , on peut essayer de convertir la première lettre d'un mot en majuscule. 
# En Pyspark, il n'exite pas de fonction permetant de le faire. Il faut donc écri
#################################################################################################################################
# import 
from pyspark.sql import SparkSession

#Initialisation 
spark = SparkSession.builder.appName('UDF en Spark').getOrCreate()

# importer un csv en dataframe 
df = spark.read.csv ('Data/cereal.csv', header=True, sep =';', inferSchema=True)
df.show()