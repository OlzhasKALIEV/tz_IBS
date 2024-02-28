import pytest
from selenium import webdriver

from pags.ibs_page import IbsHomePage
from src.api_ibs import ApiIBS
from src.settings import base_settings


@pytest.fixture
def settings():
    return base_settings


@pytest.fixture
def user_client(settings):
    api_request = ApiIBS(settings)
    return api_request


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    page_ibs = IbsHomePage(driver)
    page_ibs.open()
    yield page_ibs
    driver.quit()

