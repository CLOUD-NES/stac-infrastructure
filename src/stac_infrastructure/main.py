import stac_fastapi.geoparquet
import stac_fastapi.geoparquet.api

# empty settings, allowing configuration via environment variables
settings = stac_fastapi.geoparquet.Settings()
api = stac_fastapi.geoparquet.api.create(settings=settings)
app = api.app
