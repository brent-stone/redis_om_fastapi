"""
Primary FastAPI app instance instantiation and setup.
This will typically be called by __main__.py's implicit instantiation or directly by
Alembic and Pytest.
"""
from fastapi import FastAPI
from fastapi_redis_om.api import api_router_v1
from fastapi_redis_om.version import __version__ as webapp_version


def get_application() -> FastAPI:
    """
    Instantiate the FastAPI server instance
    :return: An instantiated FastAPI instance
    """

    _app = FastAPI(title="FastAPI + Redis OM Demo", version=webapp_version)

    _app.include_router(api_router_v1)

    return _app


app = get_application()
