"""
Redis client
https://github.com/redis/redis-om-python/blob/main/docs/connections.md#connection-objects
"""
from aredis_om import get_redis_connection
from redis import Redis
from fastapi_redis_om.core.config import core_config

redis_client: Redis = get_redis_connection(url=str(core_config.REDIS_DSN))
