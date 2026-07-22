# CLOUD-NES STAC API - Infrastructure

> [!WARNING]
> This repository is work in progress, its content could change at any time.

This repository hosts material related to the deployment of the STAC API that will index the datasets hosted on SURF as part of the [CLOUD-NES project](https://tdcc.nl/projects/tdcc-nes-projects/cloud-nes-facilitating-cloud-native-data-access-and-processing-for-nes/).

The STAC API is based on the [stac-fastapi-geoparquet](https://github.com/stac-utils/stac-fastapi-geoparquet) implementation, which serves a static STAC catalog defined in [`data/collections.json`](./data/collections.json).

## Development

### Testing the STAC API locally

* Start a test STAC API instance:
  ```shell
  docker compose up test-app
  ```
  The STAC API should be running at http://localhost:8000/ (explore via [the STAC Browser](https://radiantearth.github.io/stac-browser) at [this link](https://radiantearth.github.io/stac-browser/#/external/http:/localhost:8000/)).

* Test the API with the same `ROOT_PATH` settings used in the production deployment (see below), where the API is served behind an nginx reverse proxy under the `/stac/v1` path:
  ```shell
  docker compose up app
  ```
  The STAC API should still be reachable at http://localhost:8000/, but links in the responses will be generated as if served at `/stac/v1`, matching the production setup.

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
* Fill in the required component name (e.g. `CLOUD-NES STAC`) and description, then click "CONTINUE".
* No component parameters are required, click "CONTINUE".
* Fill in the required settings for CO ownership/visibility, then click "SUBMIT".

In order to create the **catalog item** based on the just-created component:

* On the [SRC Portal](https://portal.live.surfresearchcloud.nl/), select the "Development" tab from the top menu, then select the "Catalog Items" tab.
* Search for the "Docker Environment" catalog item, select it and click "Clone". A wizard will guide you through the generation of a new catalog item based on the configurations of the "Docker Environment" catalog item.
* Among the "Available Components" (lower menu), search for the previously-generated component (e.g. `CLOUD-NES STAC`) and click "SELECT". Make sure the list of the "Selected Components" (upper menu) includes the following elements, in this order:

  * SRC-OS
  * SRC-CO
  * SRC-Nginx
  * SRC-External plugin
  * Docker Environment
  * the previously-generated (e.g. `CLOUD-NES STAC`)

  then click "CONTINUE".
* Fill in the required catalog item name / description, then click "CONTINUE".
* Select the desired CO ownership / contact information, then click "CONTINUE".
* Select the desired catalog item visibility, then click "CONTINUE".
* Leave the cloud settings unchanged, then click "CONTINUE".
* Leave the workspace settings unchanged, then click "SUBMIT".

## Credits

* [stac-fastapi-geoparquet](https://github.com/stac-utils/stac-fastapi-geoparquet).
* Example collections are derived from [the AHN project](https://www.ahn.nl/) and [Beeldmateriaal.nl](https://beeldmateriaal.nl/).
