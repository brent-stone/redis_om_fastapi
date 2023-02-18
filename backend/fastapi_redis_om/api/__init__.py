"""
Cumulative routes from all API versions
"""
from fastapi import APIRouter
from fastapi_redis_om.api.v1.routes.route_redis_om_demo import person_router

api_router_v1 = APIRouter(prefix="/v1")

api_router_v1.include_router(person_router, prefix="/person", tags=["Person"])
