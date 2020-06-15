# tweetoffds15

## Installation 

Download the repo and naviate there from the command line:

```sh
git clone git@github.com:macrotentional/tweetoffds15.git
cd tweetoffds15
```


## Setup

Setup and activate a virtual environment:

```sh
pipenv install
pipenv shell
```

Setup the database:

## Creating and migrating the database:


```sh
FLASK_APP=web_app flask db init #> generates app/migrations dir
```

# run both when changing the schema:

```
FLASK_APP=web_app flask db migrate #> creates the db (with "alembic_version" table)
FLASK_APP=web_app flask db upgrade #> creates the specified tables
```

## Usage 

Run the web app:

```sh
FLASK_APP=web_app flask run
```
