"""
FastAPI App primary global configuration which primarily relies upon .env file provided
values.
"""
from fastapi_redis_om.version import __version__ as webapp_version
from enum import Enum
from logging import captureWarnings
from logging import getLogger
from logging.config import dictConfig
from pydantic import BaseSettings
from pydantic import Field
from pydantic import RedisDsn


class LogLevel(str, Enum):
    """
    Explicit enumerated class for acceptable Uvicorn log levels.
    This type is primarily consumed by the core_logger setup.
    """

    critical = "critical"
    error = "error"
    warning = "warning"
    info = "info"
    debug = "debug"


class CoreConfig(BaseSettings):
    """
    Primary Pydantic parser for environment variables used throughout the API layer.

    Note: Pydantic's BaseSettings class will automatically pull in environmental
    values when setting the 'env' flag in Field.
    """

    DEBUG: bool = Field(False, env="DEBUG")
    LOG_LEVEL: LogLevel = Field(LogLevel.warning, env="LOG_LEVEL")

    PROJECT_NAME: str = Field("FastAPI + Redis OM Demo", env="PROJECT_NAME")
    PROJECT_VERSION: str = Field(webapp_version, env="PROJECT_VERSION")

    REDIS_DSN: RedisDsn = Field("redis://redis-stack/0", env="REDIS_OM_URL")


core_config = CoreConfig()


LOG_CONFIG = {
    "version": 1,
    # "disable_existing_loggers": True,
    "formatters": {
        "default": {
            "format": "%(levelname)s:\t [%(filename)s:%(funcName)s:%(lineno)d]:\t %(message)s"
        }
    },
    "handlers": {
        "console": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "level": core_config.LOG_LEVEL.upper(),
        }
    },
    "root": {"handlers": ["console"], "level": core_config.LOG_LEVEL.upper()},
    "loggers": {
        "gunicorn": {"propagate": True},
        "gunicorn.access": {"propagate": True},
        "gunicorn.error": {"propagate": True},
        "uvicorn": {"propagate": True},
        "uvicorn.access": {"propagate": True},
        "uvicorn.error": {"propagate": True},
        # https://docs.celeryq.dev/en/stable/userguide/tasks.html#logging
        "celery": {"propagate": True},
        "celery.task": {"propagate": True},
        "celery.app.trace": {"propagate": True},
    },
}

captureWarnings(True)
dictConfig(LOG_CONFIG)
core_logger = getLogger(__name__)
core_logger.debug(str(core_config))
