from fastapi.responses import ORJSONResponse


app_config = dict(
    title="Language Flash Cards",
    docs_url="/docs",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
    description="Language Flash Cards Service",
    version="0.1.0",
)
