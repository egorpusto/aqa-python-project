import pytest
from utils.api_client import ApiClient


@pytest.fixture
def api_client():
    base_url = "https://reqres.in"
    api_key = "pub_b6497b14c1a18fb6931d6cbe0c949445"
    yield ApiClient(base_url, api_key)