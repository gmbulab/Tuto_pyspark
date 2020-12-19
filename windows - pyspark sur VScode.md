# Installer et utiliser Spark avec VScode sur Windows

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
  *  Par exemple si vous le dézipper dans C:\spark\spark-1.6.2-bin-hadoop2.7 ajouter C:\spark\spark-1.6.2-bin-hadoop2.6 dans les variables d'environnement. Nous appellerons ce lien le SPARK_HOME (Les version de spark et hadoop sont variables selon la version téléchargés). 
* Telecharger le winutils.exe correspondant à le version de Hadoop utilisée : https://github.com/steveloughran/winutils
  * Enregister le winutils.exe dans %SPARK_HOME%\bin
  
4.Pour utiliser Spark avec VScode : 
* Installer VScode : https://code.visualstudio.com/download
* Première Possibilité : 
  * Aller dans File >> préférence >> setting >> {chercher 'ENV: windows' dans la barre de recherche} >> Edit in settings.json
  * Ajouter le SPARK_HOME  : 
  "terminal.integrated.env.windows": {
        "SPARK_HOME" = "C:\\Users\\gmbul\\spark-3.0.1-bin-hadoop2.7\\spark-3.0.1-bin-hadoop2.7"
    }
    
   * Fermez VScode , installer pyspark en tapant 'conda install -c conda-forge pyspark' dans anaconda prompt ou 'pip install pyspark' depuis un terminal
   * Redémarez VScode et testez le code 
   
* Seconde possibilité 
  * installer findpark en ouvrant anaconda prompt et taper la commande : 'python -m pip install findspark'

Vous pouvez réaliser les tests suivant pour être sûr que ça fonctionne correctement : 
* Code obligatoire avant d'utiliser spark : # Uniquement si vous aves choisit la seconde solution avec findspark
     import findspark
     findspark.init() 
     
* Test du code : 
    import pyspark
    
    from pyspark.sql import SparkSession
    
    spark = SparkSession.builder.getOrCreate()
    
    df = spark.sql("select 'spark' as hello ")
    
    df.show()

