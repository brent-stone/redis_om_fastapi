"""
Pydantic + Redis OM schemas for REST endpoint requests and responses.
These both document the expected data for bi-directional communication with clients and
provide validation that clients and this server meet those expectations.

These schemas will generally be paired with
1. SQLAlchemy models in database.models
    Those models will typically be called by...
2. SQLAlchemy focused CRUD functions in database.repository
    Those functions will typically be called by...
3. FastAPI routes in api.*.routes
    Those routes will typically use these Pydantic schemas to document their input and
    output with clients and convert to and from the SQLAlchemy models.
"""
