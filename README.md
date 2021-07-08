# Eight queen recursive solution

1. postgresql
2. flask-cli
3. flask
4. docker-compose
5. pytest

Example of solution puzzles eight queen problem. 



To run:

```
$ docker-compose up -d --build
```

Look 127.0.0.1:5000

To run test

```
$  docker-compose exec web python manage.py test
```

Is a small test of a class call eigthqueen

To run cli eightqueen solution 

```
$ docker-compose exec web python manage.py cliejecucion --nq 8
```

nq = number of queen 

Postgresql access

```
$ docker-compose exec db psql --username=cuenca --dbname=reinasporocho
```

