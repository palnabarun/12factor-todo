# 12factor-todo

This is a simple TODO application to show the 12 Factor app patterns in action in Python.

## Backing Services

The app depends on just Postgres. Any version of modern Postgres would do. For instructions on how to install Postgres on your operating system, have a look [here](https://www.postgresql.org/docs/12/installation.html).

## Installing Dependencies

The application should run fine on Python 3.8+ as of September 1, 2020

```
$ git clone https://github.com/palnabarun/12factor-todo.git
$ cd 12factor-todo
$ python -m pip install pipenv
$ python -m pipenv install
```

## Setting up the database

Once Postgres is installed, you have to create the database and the schema.

```
$ createdb todo
$ psql todo < schema/schema.sql
```

## Running the application

### Environment variables

| Name            | Description                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------|
| PGHOST          | Postgres server hostname. If not set, psycopg2 will use the Postgres unix socket.           |
| PGPORT          | Postgres server port. If host is set and port is not set, 5432 will be used as the default. |
| PGUSER          | Postgres server username. If not set, takes in the current OS user.                         |
| PGPASSWORD      | Password for the above Postgres User. Empty if not set.                                     |
| PGDATABASE      | Database name for the application. MUST BE SET.                                             |
| WEB_CONCURRENCY | The number of workers uvicorn should spin up. If not set, 1 worker is spun up.              |
|                 |                                                                                             |

```
$ PGDATABASE=todo ./run_server.sh [--reload]
```

> Optionally, you can pass in --reload to have the server live reload on changes.

## Using the Docker image

With every tagged release of this GitHub repository a new Docker container is pushed to GitHub Container Registry.
You can pull in and use the same.

```
$ docker pull ghcr.io/palnabarun/12factor-todo:<latest|tag>
$ docker run --rm \
    --name 12factor
    --publish 8000:8000
    --env PGHOST=db.foo.com
    --env PGPORT=5432
    --env PGUSER=baz
    --env PGPASSWORD=qux
    --env PGDATABASE=todo
    ghcr.io/palnabarun/12factor-todo:<latest|tag>
```

## Talk

This app was built to show the [12factor](//12factor.net) patterns in PyCon India 2020. The draft presentation can be seen [here](https://www.nabarun.in/talk/2020/pyconindia/12-factor-snake/).

## License

This project is governed by the terms [GNU GPLv3](LICENSE.md)
