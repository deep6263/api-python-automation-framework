import allure
import pytest

from utils.response_validator import assert_response_time
from utils.schema_validator import validate_schema


@allure.feature("Posts API")
class TestPostsGet:

    @allure.story("Retrieve posts")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_get_all_posts(self, posts_api):
        response = posts_api.get_posts()

        assert response.status_code == 200

        posts = response.json()

        assert isinstance(posts, list)
        assert len(posts) > 0

    @allure.story("Retrieve post by ID")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_get_post_by_id(self, posts_api):
        response = posts_api.get_post(1)

        assert response.status_code == 200
        assert_response_time(response)

        post = response.json()

        assert post["id"] == 1
        assert post["userId"] == 1
        assert "title" in post
        assert "body" in post

    @allure.story("Retrieve non-existing post")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_get_non_existing_post(self, posts_api):
        response = posts_api.get_post(9999)

        assert response.status_code == 404

    @allure.story("Validate post schema")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_get_post_matches_schema(self, posts_api, post_schema):
        response = posts_api.get_post(1)

        assert response.status_code == 200

        validate_schema(response.json(), post_schema)