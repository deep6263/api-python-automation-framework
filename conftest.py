import pytest
from config.config import config
from clients.base_api_client import BaseApiClient
from clients.posts_api import PostsApi
from utils.data_loader import load_json
from pathlib import Path
import json

SCHEMA_DIR = Path(__file__).resolve().parent / "schemas"

@pytest.fixture
def api_client():
    return BaseApiClient(config.base_url)

@pytest.fixture
def posts_api(api_client):
    return PostsApi(api_client)

@pytest.fixture
def post_test_data():
    return load_json("posts.json")


@pytest.fixture
def post_schema():
    schema_path = SCHEMA_DIR / "posts_schema.json"

    with open(schema_path, encoding="utf-8") as file:
        return json.load(file)