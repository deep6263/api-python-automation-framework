import pytest
import allure

@allure.feature("Posts API")
class TestPostsWrite:
    @allure.story("Create post")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_create_post(self, posts_api, post_test_data):
        payload = post_test_data["valid_post"]

        response = posts_api.create_post(payload)

        assert response.status_code == 201

        created_post = response.json()

        assert created_post["title"] == payload["title"]
        assert created_post["body"] == payload["body"]
        assert created_post["userId"] == payload["userId"]

    @allure.story("Update post")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_update_post(self, posts_api, post_test_data):
        payload = post_test_data["update_post"]

        response = posts_api.update_post(1, payload)

        assert response.status_code == 200

        updated_post = response.json()

        assert updated_post["id"] == 1
        assert updated_post["title"] == payload["title"]
        assert updated_post["body"] == payload["body"]

    @allure.story("Patch post")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_patch_post(self, posts_api, post_test_data):
        payload = post_test_data["patch_post"]

        response = posts_api.patch_post(1, payload)

        assert response.status_code == 200

        patched_post = response.json()

        assert patched_post["id"] == 1
        assert patched_post["title"] == payload["title"]

    @allure.story("Delete post")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_delete_post(self, posts_api):
        response = posts_api.delete_post(1)

        assert response.status_code == 200