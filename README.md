# CLOUD-NES STAC API - Infrastructure

> [!WARNING]
> This repository is work in progress, its content could change at any time.

This repository hosts material related to the deployment of the STAC API that will index the datasets hosted on SURF as part of the [CLOUD-NES project](https://tdcc.nl/projects/tdcc-nes-projects/cloud-nes-facilitating-cloud-native-data-access-and-processing-for-nes/).

The STAC API is based on the [stac-fastapi-pgstac](https://github.com/stac-utils/stac-fastapi-pgstac) implementation.

## Development

### Testing the STAC API locally

* Generate the `.env` configuration file from the given template:

  ```shell
  cp .env.template .env
  # edit the .env file
  ```

* Start a test STAC API instance and ingest a test dataset, using the [transaction extension](https://github.com/stac-api-extensions/transaction):

  ```shell
  docker compose up ingest-test-data
  ```

  The STAC API should be running at http://localhost:8082/ (explore via [the STAC Browser](https://radiantearth.github.io/stac-browser) at [this link](https://radiantearth.github.io/stac-browser/#/external/http:/localhost:8082/)).


* Test the production STAC API deployment, including the nginx reverse proxy, and ingest a test dataset using [`pypgstac`](https://stac-utils.github.io/pgstac/pypgstac/), which bypasses the FastAPI interface and connects directly to the database:

  ```shell
  docker compose up nginx ingest-data
  ```

  The STAC API should be running at http://localhost/stac/v1 (explore via [the STAC Browser](https://radiantearth.github.io/stac-browser) at [this link](https://radiantearth.github.io/stac-browser/#/external/http:/localhost/stac/v1/)).


* Stop all services, cleaning up stopped containers:

  ```shell
  docker compose rm --stop --force
  ```
