# Installer et utiliser Spark sur Jupyter Notebook sur Windows

1.	Voir la version de Java : 
*	Java -version
*	Si Java n’est pas installée, télécharger et installer java : https://www.java.com/fr/download/win10.jsp

2.	Voir la version de Python
*	Python –version
*	Si Python n’est pas installé et que vous n'utilisez pas une distribution telque Anaconda, télécharger et installer Python : https://www.python.org/downloads/windows/

3. Télécharger Spark : http://spark.apache.org/downloads.html
* choisir une "spark relase" et un "package type"
* choisir un mode de téléchargement
* Dézipper le fichier téléchargé et ajouter le lien dans les variables d'environnement  : 
  *  Par exemple si vous le dézipper dans C:\spark\spark-1.6.2-bin-hadoop2.6 ajouter C:\spark\spark-1.6.2-bin-hadoop2.6 dans les variables d'environnement. Nous appellerons ce lien le SPARK_HOME
* Telecharger le winutils.exe correspondant à le version de Hadoop utilisée : https://github.com/steveloughran/winutils
  * Enregister le winutils.exe dans %SPARK_HOME%\bin
  
4.Pour utiliser Spark avec Jupyter Notebook : 
* Installer Jupyter Notebook via Anaconda (plus simple)
* Ouvrir anaconda prompt et taper la commande : '**python -m pip install findspark**'
* Lancer ensuite jupyter notebook en tapant '**jupyter notebook**' dans ananconda prompt 

Vous pouvez réaliser les tests suivant pour être sûr que ça fonctionne correctement : 
* Code obligatoire avant d'utiliser spark : 
     import findspark
     
     findspark.init()
* Teste du code : 
    import pyspark
    
    from pyspark.sql 
    
    import SparkSession
    
    spark = SparkSession.builder.getOrCreate()
    
    df = spark.sql("select 'spark' as hello ")
    
    df.show()
