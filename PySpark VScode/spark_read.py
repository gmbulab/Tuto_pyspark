###################################################################
# Créer à Dataframe à partir d'un csv, Json etc
###################################################################

# Import 
from pyspark.sql import SparkSession

# Initialisation de le Sparksession

spark = SparkSession.builder.appName('Spark read').getOrCreate()

##### La syntaxe : 
#### Lire un csv
### spark.read.csv('path_to_csv') ou spark.read.format("csv").load("path") : renvoie un dataframe
# Ici les colonnes seront nommées de _C0 à _C1
# Les colonnes sont de types strings par défaut 
df_csv1 = spark.read.csv('/Data/cereal.csv')
df_csv2 = spark.read.format("csv").load("/Data/cereal.csv")

### Les options
# header : noms des colonnes sur la première ligne
df_csv1 = spark.read.option('header', 'true').csv('../Data/cereal.csv') # Lire les noms de colonnes sur la première ligne
df_csv2 =  spark.read.format("csv").options(header='true').load('Data/cereal.csv')
df_csv2.show()

