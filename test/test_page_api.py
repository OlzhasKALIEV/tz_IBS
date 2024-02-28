from utils.constants.routes import APIRoutes


def test_click_get_list_users(browser, user_client):
    page = "2"
    response_api = user_client.get(APIRoutes.LIST_USERS + page)
    response_page = browser.click_get_list_users()
    assert response_page == response_api


def test_click_get_single_user(browser, user_client):
    id_user = "2"
    response_api = user_client.get(APIRoutes.USERS + id_user)
    response_page = browser.click_get_single_user()
    assert response_page == response_api


def test_click_get_single_user_not_found(browser, user_client):
    id_user = "23"
    response_api = user_client.get(APIRoutes.USERS + id_user, 404)
    response_page = browser.click_get_single_user_not_found()
    assert response_page == response_api
