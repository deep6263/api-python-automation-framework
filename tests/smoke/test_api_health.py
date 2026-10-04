import allure
import pytest


@allure.feature("API Health")
@allure.story("API availability")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
def test_api_is_available(posts_api):
    response = posts_api.get_post(1)

    assert response.status_code == 200