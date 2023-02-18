"""
Demo v1 REST endpoints for Redis OM integration
"""
from fastapi import APIRouter
from fastapi import status
from fastapi_redis_om.schemas.schema_redis_om_demo import Person
from fastapi_redis_om.schemas.schema_redis_om_demo import PersonAllResponse

person_router = APIRouter()


@person_router.post(
    "/create",
    response_model=Person,
    status_code=status.HTTP_201_CREATED,
)
async def create_person(a_person: Person) -> Person:
    """
    Attempt to create a new Person entry in the Redis backend
    :param a_person: The person schema
    :type a_person: Person
    :return: The same schema on success; 40* response on error
    :rtype: Person
    """
    return await a_person.save()


@person_router.get(
    "/persons",
    response_model=PersonAllResponse,
    status_code=status.HTTP_200_OK,
)
async def get_persons() -> PersonAllResponse:
    """
    Attempt to retrieve all Person records
    :return: PersonAllResponse
    :rtype: PersonAllResponse
    """
    l_pks = [pk async for pk in await Person.all_pks()]
    return PersonAllResponse(persons=l_pks)
