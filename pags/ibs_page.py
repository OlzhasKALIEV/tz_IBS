import json

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pags.base_page_ibs import BasePage


class IbsHomePage(BasePage):
    COMMON_SELECTOR = 'a[data-key="try-link"]'

    LIST_USERS = (By.CSS_SELECTOR, 'li[data-id="users"] ' + COMMON_SELECTOR)
    SINGLE_USERS = (By.CSS_SELECTOR, 'li[data-id="users-single"] ' + COMMON_SELECTOR)
    SINGLE_USER_NOT_FOUND = (
        By.CSS_SELECTOR,
        'li[data-id="users-single-not-found"] ' + COMMON_SELECTOR,
    )
    LIST_RESOURCE = (By.CSS_SELECTOR, 'li[data-id="unknown"] ' + COMMON_SELECTOR)
    SINGLE_RESOURCE = (
        By.CSS_SELECTOR,
        'li[data-id="unknown-single"] ' + COMMON_SELECTOR,
    )
    SINGLE_RESOURCE_NOT_FOUND = (
        By.CSS_SELECTOR,
        'li[data-id="unknown-single-not-found"] ' + COMMON_SELECTOR,
    )
    CREATE = (By.CSS_SELECTOR, 'li[data-id="post"] ' + COMMON_SELECTOR)
    UPDATE_PUT = (By.CSS_SELECTOR, 'li[data-id="put"] ' + COMMON_SELECTOR)
    UPDATE_PATCH = (By.CSS_SELECTOR, 'li[data-id="patch"] ' + COMMON_SELECTOR)
    DELETE = (By.CSS_SELECTOR, 'li[data-id="delete"] ' + COMMON_SELECTOR)
    REGISTER_SUCCESSFUL = (
        By.CSS_SELECTOR,
        'li[data-id="register-successful"] ' + COMMON_SELECTOR,
    )
    REGISTER_UNSUCCESSFUL = (
        By.CSS_SELECTOR,
        'li[data-id="register-unsuccessful"] ' + COMMON_SELECTOR,
    )
    LOGIN_SUCCESSFUL = (
        By.CSS_SELECTOR,
        'li[data-id="login-successful"] ' + COMMON_SELECTOR,
    )
    LOGIN_UNSUCCESSFUL = (
        By.CSS_SELECTOR,
        'li[data-id="login-unsuccessful"] ' + COMMON_SELECTOR,
    )
    DELAYED_RESPONSE = (By.CSS_SELECTOR, 'li[data-id="delay"] ' + COMMON_SELECTOR)

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

    def click_get_list_resource(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LIST_RESOURCE)
        )
        element.click()
        response_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.OUTPUT_RESPONSE)
        )
        return json.loads(response_element.text)

    def click_get_single_resource(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SINGLE_RESOURCE)
        )
        element.click()
        response_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.OUTPUT_RESPONSE)
        )
        return json.loads(response_element.text)

    def click_get_single_resource_not_found(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SINGLE_RESOURCE_NOT_FOUND)
        )
        element.click()
        response_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.OUTPUT_RESPONSE)
        )
        return json.loads(response_element.text)

    def click_post_create(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CREATE)
        )
        element.click()
        response_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.OUTPUT_RESPONSE)
        )
        return json.loads(response_element.text)

    def click_put_update(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.UPDATE_PUT)
        )
        element.click()
        response_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.OUTPUT_RESPONSE)
        )
        return json.loads(response_element.text)

    def click_patch_update(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.UPDATE_PATCH)
        )
        element.click()
        response_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.OUTPUT_RESPONSE)
        )
        return json.loads(response_element.text)

    def click_delete(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.DELETE)
        )
        element.click()
        response_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.OUTPUT_RESPONSE)
        )
        response_text = response_element.text.strip() if response_element.text else None
        return response_text

    def click_post_register_successful(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.REGISTER_SUCCESSFUL)
        )
        element.click()
        response_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.OUTPUT_RESPONSE)
        )
        return json.loads(response_element.text)

    def click_post_register_unsuccessful(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.REGISTER_UNSUCCESSFUL)
        )
        element.click()
        response_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.OUTPUT_RESPONSE)
        )
        return json.loads(response_element.text)

    def click_post_login_successful(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGIN_SUCCESSFUL)
        )
        element.click()
        response_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.OUTPUT_RESPONSE)
        )
        return json.loads(response_element.text)

    def click_post_login_unsuccessful(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGIN_UNSUCCESSFUL)
        )
        element.click()
        response_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.OUTPUT_RESPONSE)
        )
        return json.loads(response_element.text)

    def click_get_delay(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.DELAYED_RESPONSE)
        )
        element.click()
        response_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.OUTPUT_RESPONSE)
        )
        return json.loads(response_element.text)
