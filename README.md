# CLOUD-NES STAC Catalog - Infrastructure

> [!WARNING]
> This repository is work in progress, its content could change at any time.

This repository hosts material related to the deployment of a STAC API for the datasets hosted on SURF as part of the CLOUD-NES project.

The STAC API is run by a FastAPI application based on the [stac-fastapi-pgstac](https://github.com/stac-utils/stac-fastapi-pgstac) implementation.

## Development

### Running the STAC API locally

Generate the `.env` configuration file from the given template:

```shell
cp .env.template .env
# edit the .env file
```

Start a test STAC API instance and ingest a test dataset with:

```shell
docker compose run --rm ingest-test-data
```

The STAC API should be running at http://localhost:8082/ (explore via [the STAC Browser](https://radiantearth.github.io/stac-browser) at [this link](https://radiantearth.github.io/stac-browser/#/external/http:/localhost:8082/)).


Test the production STAC API deployment, including the nginx reverse proxy:

```shell
docker compose up nginx
```

The STAC API should be running at http://localhost/stac/v1 (explore via [the STAC Browser](https://radiantearth.github.io/stac-browser) at [this link](https://radiantearth.github.io/stac-browser/#/external/http:/localhost/stac/v1/)).


Once the STAC API is running, ingest all the records as:

```shell
docker compose run --rm ingest-data
```

Stop all services, cleaning up stopped containers:

```shell
docker compose rm --stop --force
```