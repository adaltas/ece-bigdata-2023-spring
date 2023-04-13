1. Creer un csv:
````
id,author,genre,quantity
1,hunter.fields,romance,15
2,leonard.lewis,thriller,81
3,jason.dawson,thriller,90
4,andre.grant,thriller,25
5,earl.walton,romance,40
6,alan.hanson,romance,24
7,clyde.matthews,thriller,31
8,josephine.leonard,thriller,1
9,owen.boone,sci-fi,27
10,max.mcBride,romance,75
```
=========



2. Charger le csv en dataframe dans Spark

3. Le nombre d'ecrit par genre


4. Ranking number des auteurs par nombre de livre ecrit:

Ex:
ranking,author,genre,quantity
1,jason.dawson,thriller,90
2,leonard.lewis,thriller,81
3,max.mcBride,romance,75
4,earl.walton,romance,40
5,clyde.matthews,thriller,31
6,owen.boone,sci-fi,27
7,andre.grant,thriller,25
8,alan.hanson,romance,24
9,hunter.fields,romance,15
10,josephine.leonard,thriller,1

5. Renommer les noms en version "standard" 'jason.dawson' => 'Jason Dawson'

https://sparkbyexamples.com/spark/spark-sql-window-functions/


6. Charger l'ensemble suivant

val input = Seq(
  ("100","John", Some(35),None),
  ("100","John", None,Some("Georgia")),
  ("101","Mike", Some(25),None),
  ("101","Mike", None,Some("New York")),
  ("103","Mary", Some(22),None),
  ("103","Mary", None,Some("Texas")),
  ("104","Smith", Some(25),None),
  ("105","Jake", None,Some("Florida"))).toDF("id", "name", "age", "city")

scala> input.show
+---+-----+----+--------+
| id| name| age|    city|
+---+-----+----+--------+
|100| John|  35|    null|
|100| John|null| Georgia|
|101| Mike|  25|    null|
|101| Mike|null|New York|
|103| Mary|  22|    null|
|103| Mary|null|   Texas|
|104|Smith|  25|    null|
|105| Jake|null| Florida|
+---+-----+----+--------+


7. fusionner les cellules de meme id:

scala> solution.show()
+---+-----+----+--------+
|id |name |age |city    |
+---+-----+----+--------+
|100|John |35  |Georgia |
|101|Mike |25  |New York|
|103|Mary |22  |Texas   |
|104|Smith|25  |null    |
|105|Jake |null|Florida |
+---+-----+----+--------+