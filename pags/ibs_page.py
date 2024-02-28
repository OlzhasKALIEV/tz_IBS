import json

import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IbsHomePage:
    LIST_USERS = (By.CSS_SELECTOR, 'a[href="/api/users?page=2"]')
    SINGLE_USERS = (By.CSS_SELECTOR, 'a[href="/api/users/2"]')
    OUTPUT_RESPONSE = (By.CSS_SELECTOR, 'pre[data-key="output-response"]')

    def __init__(self, driver, settings) -> None:
        self.driver = driver
        self.settings = settings
        self.session = requests.session()

    def open(self) -> None:
        self.driver.get(self.settings.base_url)

    def scroll_list_users(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.LIST_USERS)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_get_list_users(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LIST_USERS)
        )
        element.click()
        response_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.OUTPUT_RESPONSE)
        )
        return json.loads(response_element.text)

    def click_get_single_user(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SINGLE_USERS)
        )
        element.click()
        response_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.OUTPUT_RESPONSE)
        )
        return json.loads(response_element.text)


# ibs_home_page = IbsHomePage(base_settings)
#
# # Откройте ссылку с помощью метода open
# ibs_home_page.open()
# ibs_home_page.scroll_list_users()
# ibs_home_page.click_get_list_users()
# ibs_home_page.click_get_single_user()
