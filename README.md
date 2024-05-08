# Docker 101 Demo
Demo for Dibimbing.id MSIB Batch 6 about Introduction to Docker. The `docker-compose.yml` file is taken from [here](https://github.com/ClickHouse/examples/blob/main/docker-compose-recipes/recipes/ch-and-postgres/docker-compose.yaml)

# Requirements
1. Install [Docker Engine](https://docs.docker.com/engine/install/) or [Docker Desktop](https://docs.docker.com/desktop/)
2. Install [Docker Compose](https://docs.docker.com/compose/install/)

# Environment Files
Please define this variable on your `.env` that will be used by docker-compose.

```
PG_USER=<your-pg-user>
PG_PASSWORD=<your-pg-password>
PG_DB=<your-db>
```