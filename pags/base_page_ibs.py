from src.settings import base_settings


class BasePage:

    page_url = ""

    def __init__(self, driver) -> None:
        self.driver = driver

    def open(self) -> None:
        self.driver.get(base_settings.base_url + self.page_url)
