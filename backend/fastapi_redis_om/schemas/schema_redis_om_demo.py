"""
Pydantic+Redis OM schemas paired with the route_redis_om_demo route
"""
from aredis_om import EmbeddedJsonModel, Field, JsonModel
from pydantic import PositiveInt
from typing import Optional, List, Any
from fastapi_redis_om.core.redis import redis_client


class Address(EmbeddedJsonModel):
    """
    Demo Redis OM nested Pydantic model for Address as a subset of Person
    """
    street_number: PositiveInt = Field(index=True)

    # Unit isn't in all addresses, so let's make it optional
    # and not index it.
    unit: Optional[str] = Field(index=False)
    street_name: str = Field(index=True)
    city: str = Field(index=True)
    state: str = Field(index=True)
    postal_code: str = Field(index=True)

    # Provide a default value if none supplied...
    country: str = Field(index=True, default="United Kingdom")

    class Meta:
        """
        Modify the default Redis server connection
        """
        database = redis_client


class Person(JsonModel):
    """
    Demo Redis OM Pydantic model for Person
    """
    # Indexed for exact text matching
    first_name: str = Field(index=True)
    last_name: str = Field(index=True)

    # Indexed for numeric matching
    age: PositiveInt = Field(index=True)

    # Use an embedded sub-model
    address: Address

    skills: List[str] = Field(index=True)

    # Indexed for full text search
    personal_statement: str = Field(index=True, full_text_search=True)

    class Meta:
        """
        Modify the default Redis server connection
        """
        database = redis_client


class PersonAllResponse(JsonModel):
    """
    Demo Redis OM Pydantic model for retrieving all Person records
    """
    persons: List[str] = Field(index=False)

    class Meta:
        """
        Modify the default Redis server connection
        """
        database = redis_client
