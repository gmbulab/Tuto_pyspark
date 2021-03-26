#################################################
# Quelques fonctions Pyspark avec les Dataframes

# Imports 
import sys

# Initialisation
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Dataframe').getOrCreate()


# Import df
df = spark.read.csv('..\\..\\..\\Data_used\\appl_stock.csv', inferSchema = True, header = True)
df.printSchema()

# Filter Data where clise >50
df_filt =  df.filter('Close<50')
print(df_filt.show())

# use select to select a column
# First select 
df1 = df.select('Date')
print(df1.show()) 

# Filter and select 
df2 =  df.filter ('Close<50').select("Open")
print(df2.show())

# Select two or morecolumns 
df3 = df.select(['Date', 'Open'])
print(df3.show())


# Filter in python way 
df4 = df.filter(df['close']<50)
df4.show()

# Multiple filtre : # Parenthèses pour séparer les différentes conditions
df5 = df.filter((df['close']<50) & (df['Open']>200)) 
df5.show()

# Same in SQL 
print(">>>>>>>>>>>>>>>>>> SQL Select Dataframe >>>>>>>>>>>>>>>>>>>>>>>>")
# la première étape est de créer le df comme une vue
df.createOrReplaceTempView("vue_df")
df_filt_sql = spark.sql('select * from vue_df where Close<50')
df2_sql = spark.sql('select Open from vue_df where Close<50')

print(df_filt_sql.show())
print(df2_sql.show())



