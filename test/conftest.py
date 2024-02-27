import pytest

from src.api_ibs import ApiIBS
from src.settings import base_settings


@pytest.fixture
def settings():
    return base_settings


@pytest.fixture
def user_client(settings):
    api_request = ApiIBS(settings)
    return api_request
