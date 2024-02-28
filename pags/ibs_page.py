import json

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pags.base_page_ibs import BasePage


class IbsHomePage(BasePage):
    LIST_USERS = (By.CSS_SELECTOR, 'li[data-id="users"] a[data-key="try-link"]')
    SINGLE_USERS = (By.CSS_SELECTOR, 'li[data-id="users-single"] a[data-key="try-link"]')
    SINGLE_USER_NOT_FOUND = (By.CSS_SELECTOR, 'li[data-id="users-single-not-found"] a[data-key="try-link"]')
    OUTPUT_RESPONSE = (By.CSS_SELECTOR, 'pre[data-key="output-response"]')

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

    def click_get_single_user_not_found(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SINGLE_USER_NOT_FOUND)
        )
        element.click()
        response_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.OUTPUT_RESPONSE)
        )
        return json.loads(response_element.text)
