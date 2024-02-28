from utils.constants.routes import APIRoutes


def test_click_get_list_users(browser, user_client):
    page = "2"
    response_api = user_client.get(APIRoutes.LIST_USERS + page)
    response_page = browser.click_get_list_users()
    assert response_page == response_api
