from fastapi.responses import ORJSONResponse


db_connect_data_exception = ValueError(
    "Missing necessary data to connect to database",
)


def sqlalchemy_not_found_exception_handler(*_):
    return ORJSONResponse(
        status_code=404,
        content={
            "detail": "Resource is not found",
        },
    )
