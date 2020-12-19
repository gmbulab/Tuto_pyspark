###################################################################
# Créer à Dataframe à partir d'un csv, Json etc
###################################################################

# Import 
from pyspark.sql import SparkSession

# Initialisation de le Sparksession

spark = SparkSession.builder.appName('Spark read').getOrCreate()

##### La syntaxe : 

#### Lire un csv
### spark.read.csv('path_to_csv') : le plus simple et le plus utilisé
#  ou spark.read.format("csv").load("path") : renvoie un dataframe
#*************************************************************************************************

# Ici les colonnes seront nommées de _C0 à _C1
# Les colonnes sont de types strings par défaut 
df_csv1 = spark.read.csv('Data/cereal.csv', header=True, sep =';')

df_csv2 = spark.read.format("csv").load("Data/cereal.csv")

### Les options (liste non exhaustive)
# header : noms des colonnes sur la première ligne
# schema : un schema de type StrucType 
# InferSchema : inférer le schemas automatiquement

## Plusieurs options : le plus simple 
df = spark.read.csv('Data/cereal.csv', header=True, sep =';', inferSchema= True)
df.show()



#Soit avec .option : pas très pratique
df_csv1 = spark.read.option('header', 'true').csv('Data/cereal.csv') # Lire les noms de colonnes sur la première ligne
df_csv2 =  spark.read.format("csv").options(header='true').load('Data/cereal.csv')

#### To Do : lire plusieur csv en même temps 
# df = spark.read.csv("path1,path2,path3")
# df = spark.read.csv("Folder path")

#### Lire un json
### spark.read.json('path_to_json') ou spark.read.format("json").load("path") : renvoie un dataframe
#***************************************************************************************************

# Todo: code pour json , txt 
