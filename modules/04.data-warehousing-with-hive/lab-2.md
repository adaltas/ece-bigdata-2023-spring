# Big Data Ecosystem

## Lab 4.2: Hive Query Language

### Goals

- Write advanced HQL queries
- Optimize the queries

### Input tables

In this lab we will use the 4 IMDb datasets that are located in your group database:

- `imdb_name_basics`
- `imdb_title_basics`
- `imdb_title_crew`
- `imdb_title_ratings`

For more informations about the datasets: [IMDb Datasets](https://www.imdb.com/interfaces/).

### Queries

1. Number of titles with duration superior than 2 hours.
2. Average duration of titles containing the word "world" (but not words like "Underworld"). Hint: use `RLIKE` (see [RegExr](https://regexr.com/))
3. Average rating of titles having the genre "Comedy"
4. Average rating of titles not having the genre "Comedy"
5. Top 5 movies directed by Tarantino

For 5., you can first try to do it in 2 seperate queries. Then try to use a single query (tip: `explode` or `array_contains`)
