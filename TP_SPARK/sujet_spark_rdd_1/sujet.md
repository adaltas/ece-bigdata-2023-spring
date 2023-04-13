1. Creer un csv:
....
echo "id,nom,prenom,age" >> monfichier.txt
echo "1,sauvage,pierre,31" >> monfichier.txt

=========
2. Charger le csv en RDD dans spark

val rdd = sc.textFile("/home/pierrotws/monfichier.txt")

2b. Afficher le contenu du RDD

2c: Filtrer le rdd : supprimer les lignes dont l'age est inférieur à 18

2d: Convertir le RDD en dataframe (google est votre ami)

========

3. Charger le csv en dataframe dans Spark
3b. Afficher le contenu du rdd
3c: Filtrer le DF: supprimer les lignes dont l'age est inférieur à 18

bonus: le faire avec l'API Spark native, puis en SQL (spark.sql("..."))

3d: Afficher l'age minimal, l'age maximal, l'age moyen en API Spark DataFrame (pas spark.sql)
