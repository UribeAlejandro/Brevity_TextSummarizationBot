# Test Driven Development with Fast API & Docker

## Introduction

This project is an example of how to use Fast API with Docker and Test Driven Development to create an asynchronous text summarization API. The following endpoints are available:

| Endpoint        | HTTP Method	 | CRUD Method | Result               |
|-----------------|--------------|-------------|----------------------|
| /summaries	     | GET          | READ        | get all summaries    |
| /summaries/:id	 | GET	         | READ	       | get a single summary |
| /summaries      | 	POST        | 	CREATE     | 	add a summary       |
| /summaries/:id	 | PUT	         | UPDATE      | 	update a summary    |
| /summaries/:id	 | DELETE	      | DELETE      | 	delete a summary    |

## Table of Contents

Lorem Ipsum


## Technologies

The following technologies are used in this project:

- Fast API: A modern, batteries-included, fast (high-performance), web framework for building RESTful APIs with Python.
- Docker: A container platform used to streamline application development and deployment workflows across various environments.
- Pytest: Is a testing framework that makes it easy to write, organize, and run simple/complex tests.
- Tortoise ORM: An async ORM inspired by the Django ORM that's designed for ease of use.
- Heroku: A cloud *Platform as a Service* (PaaS) that provides hosting for web applications.

## Getting Started

To get started, you need to have `Python` & `Docker` installed on your machine. Create a new Python environment and install the required packages using the following commands:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements_dev.txt
```

Run the application locally using the following command:

```bash
uvicorn app.main:app
```

On the other hand, check your `Docker` & `Docker Compose` installation by running the following command:

```bash
docker -v
docker-compose -v
```

Then, build the Docker image and run the container (in detached mode) using the following commands:

```bash
docker-compose up -d --build
```

You can now access the application's `Docs` on `http://localhost:8000/docs`. Once done, check the logs for the web service:

```bash
docker-compose logs web
```

Create migrations using the following command:

```bash
docker-compose exec web aerich init -t app.db.TORTOISE_ORM
```

Then, apply the migrations using the following command:

```bash
docker-compose exec web aerich init-db
```

> **Note**: the command above might fail if the directory `migrations` already exists. In that case, you can remove the directory and run the command again.


Access the database, you can use the following command:

```bash
docker-compose exec web-db psql -U postgres
```

Then, you can run the following commands to check the tables:

```bash
\c web_dev
\dt
```
> **Note**: You should see two tables `aerich` & `text_summary`.

To bring down the containers and volumes to destroy the database, use the following command:

```bash
docker-compose down -v
```

## Testing

To run the tests, use the following command:

```bash
docker-compose up -d --build
docker-compose exec web python -m pytest -vv -p no:warnings
```

Test the `/summaries` endpoint using the following command:

```bash
docker-compose exec web python app/db.py
http --json POST http://localhost:8004/summaries/ url=http://testdriven.io
```

Or using curl as follows:

```bash
curl -X POST "http://localhost:8004/summaries/" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"url\":\"http://testdriven.io\"}"
```

## Deployment
