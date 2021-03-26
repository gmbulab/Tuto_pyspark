##############################################################################################################################
# Ce chapitre traite les UDF en PySpark. 
# Les UDF sont très utiles en Spark SQL, elles permettent d'étendre les fonctions de base de pyspark. 
# User Defined Function ou UDF permet à un utilisateur de créer sa propre fonction en python, 
# de l'enregistrer avec spark SQL et de l'utiliser sur des Dataframe ou en Spark SQL grâce  à udf()
# Par exemple , on peut essayer de convertir la première lettre d'un mot en majuscule. 
# En Pyspark, il n'exite pas de fonction permetant de le faire. Il faut donc écrire la fonction en python puis l'utiliser
# Les UDF sont des opérations très gourmandes en ressource. Il faut donc les utiliser uniquement lorsqu'on a pas le choix
#################################################################################################################################
# import 
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import StringType

#Initialisation 
spark = SparkSession.builder.appName('UDF en Spark').getOrCreate()
sc = spark.sparkContext
# importer un csv en dataframe 
df = spark.read.csv ('Data/cereal.csv', header=True, sep =';', inferSchema=True)


# créer une fonction en python 

def convertCase(str): 
    lowStr =""
    arr =  str.split("")
    for x in arr : 
        lowStr = lowStr + x[0:1].lower() + x[1:len(x)]
    return lowStr

# Convertir converCase en UDF en l apassant à udf() de pySpark SQl
# La syntaxe : nouveau_nom_fonction = udf(lambda z : nom_fonction, returnType) 
# Par defaut returnType est String, on peut ne rien mettre quand ça renvoie un string

convertUDF = udf(lambda z : convertCase(z), StringType()) 

# Utilisation avec un Dataframe
df = df.withColumn('name1', convertUDF('name')).show()
#df.select(col('mfr'), convertUDF(col('name'))).show()
