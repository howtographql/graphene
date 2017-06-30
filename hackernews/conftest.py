import pytest
from graphene.test import Client

from hackernews.schema import schema


@pytest.fixture
def graphql_client():
    return Client(schema)
