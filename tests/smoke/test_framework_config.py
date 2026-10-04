import pytest
import allure
from config.config import config


@allure.feature("Framework Configuration")
@allure.story("Environment configuration")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_environment_configuration():
    assert config.environment == "qa"
    assert config.environment_name == "qa"
    assert config.base_url == "https://jsonplaceholder.typicode.com"