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

### Register SURF Research Cloud Application

In order to create the catalog item that allows one to deploy the CLOUD-NES STAC API via the SURF Research Cloud (SRC) portal, one needs first to create an application **component**:

* On the [SRC Portal](https://portal.live.surfresearchcloud.nl/), select the "Development" tab from the top menu, then select the "Components" tab and click "+" to add a new Component.
* Fill in the following details, then click "CONTINUE":
  * "Component script type": Ansible PlayBook
  * "Repository URL": https://github.com/CLOUD-NES/stac-infrastructure.git
  * "Path": research-cloud-component.yml
* Fill in the required component name and description, then click "CONTINUE".
* Add two component parameters with the following details, then click "CONTINUE":
  * "Parameter key": `postgres_user`, "Source type": "Workspace", "Initial value": `username`, and tick only the "Overwritable" box.
  * "Parameter key": `postgres_password`, "Source type": "Workspace", "Initial value": `password`, and tick only the "Overwritable" box.
* Fill in the required settings for CO ownership/visibility, then click "SUBMIT".

In order to create the **catalog item** based on the just-created component:

* On the [SRC Portal](https://portal.live.surfresearchcloud.nl/), select the "Development" tab from the top menu, then select the "Catalog Items" tab.
* Search for the "Docker Environment" catalog item, select it and click "Clone". A wizard will guide you through the generation of a new catalog item based on the configurations of the "Docker Environment" catalog item.
* Among the "Available Components" (lower menu), search for the previously-generated component and click "SELECT". Make sure the component is listed as the **last element** in the "Selected Components" (upper menu), then click "CONTINUE".
* Fill in the required catalog item name / description, then click "CONTINUE".
* Select the desired CO ownership / contact information, then click "CONTINUE".
* Select the desired catalog item visibility, then click "CONTINUE".
* Leave the cloud settings unchanged, then click "CONTINUE".
* For the `postgres_user` and `postgres_password` parameters in the list, select "Make interactive" in the "Actions" column, then fill in "Postgres username" and "Postgres password" as labels, respectively. Click "CONTINUE".
* Leave the workspace settings unchanged, then click "SUBMIT".

## Credits

* [stac-fastapi-pgstac](https://github.com/stac-utils/stac-fastapi-pgstac).
* The [`wait-for-it.sh`](./scripts/wait-for-it.sh) script is taken from [this repository](https://github.com/vishnubob/wait-for-it).
* Test data is derived from [the AHN project](https://www.ahn.nl/).
