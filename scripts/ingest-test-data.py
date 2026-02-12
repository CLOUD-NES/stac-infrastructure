# /// script
# dependencies = [
#     "requests",
# ]
# ///
"""Ingest test data set into the STAC catalog.

Example usage:

```shell
uv run --script scripts/ingest-test-data.py -c testdata/AHN5.json -i testdata/AHN5_C_*.json -- http://localhost:8082/
```
"""

import argparse
import json
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

import requests


def parse_args() -> dict[str, Any]:
    """Parse input arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--collection_path",
        type=str,
        required=True,
        help="Path to the collection",
    )
    parser.add_argument(
        "-i",
        "--items_path",
        type=str,
        required=True,
        help="Path to the items",
    )
    parser.add_argument("url", type=str, help="URL of the catalog.")
    args = parser.parse_args()
    return vars(args)


def main(url: str, collection_path: str, items_path: str) -> None:
    """Ingest collection and items into the catalog at the given URL."""
    # First ingest the collection
    collection = json.loads(Path(collection_path).read_text())
    post(urljoin(url, "/collections"), data=collection)

    # Load an item from each row of the NDJSON file, then ingest it
    with Path(items_path).open() as f:
        for line in f:
            item = json.loads(line)
            post(urljoin(url, f"/collections/{collection['id']}/items"), data=item)


def post(url: str, data: dict) -> None:
    """Post data to url."""
    r = requests.post(url, json=data)
    r.raise_for_status()


if __name__ == "__main__":
    args = parse_args()
    main(**args)
