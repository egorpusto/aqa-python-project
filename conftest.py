import pytest
from dotenv import load_dotenv
import os
from utils.api_client import ApiClient

load_dotenv()

@pytest.fixture
def api_client():
    base_url = os.getenv("BASE_URL")
    api_key = os.getenv("API_KEY")
    yield ApiClient(base_url, api_key)