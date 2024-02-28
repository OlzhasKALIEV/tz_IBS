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


def test_click_get_list_resource(browser, user_client):
    response_api = user_client.get(APIRoutes.SINGLE_RESOURCE)
    response_page = browser.click_get_list_resource()
    assert response_page == response_api


def test_click_get_single_resource(browser, user_client):
    id_user = "2"
    response_api = user_client.get(APIRoutes.SINGLE_RESOURCE + id_user)
    response_page = browser.click_get_single_resource()
    assert response_page == response_api


def test_click_get_single_resource_not_found(browser, user_client):
    id_user = "23"
    response_api = user_client.get(APIRoutes.SINGLE_RESOURCE + id_user, 404)
    response_page = browser.click_get_single_resource_not_found()
    assert response_page == response_api


def test_click_post_create(browser, user_client):
    data = {"name": "morpheus", "job": "leader"}
    response_api = user_client.post(APIRoutes.USERS, data)
    response_page = browser.click_post_create()
    assert response_page["job"] == response_api["job"]
    assert response_page["name"] == response_api["name"]


def test_click_put_update(browser, user_client):
    id_user = "2"
    data = {"name": "morpheus", "job": "zion resident"}
    response_api = user_client.put(APIRoutes.USERS + id_user, data)
    response_page = browser.click_put_update()
    assert response_page["job"] == response_api["job"]
    assert response_page["name"] == response_api["name"]


def test_click_patch_update(browser, user_client):
    id_user = "2"
    data = {"name": "morpheus", "job": "zion resident"}
    response_api = user_client.patch(APIRoutes.USERS + id_user, data)
    response_page = browser.click_patch_update()
    assert response_page["job"] == response_api["job"]
    assert response_page["name"] == response_api["name"]


def test_click_delete(browser, user_client):
    id_user = "2"
    response_api = user_client.delete(APIRoutes.USERS + id_user)
    response_page = browser.click_delete()
    assert response_page == response_api


def test_click_post_register_successful(browser, user_client):
    data = {"email": "eve.holt@reqres.in", "password": "pistol"}
    response_api = user_client.post(APIRoutes.REGISTER, data, 200)
    response_page = browser.click_post_register_successful()
    assert response_page == response_api


def test_click_post_register_unsuccessful(browser, user_client):
    data = {"email": "sydney@fife"}
    response_api = user_client.post(APIRoutes.REGISTER, data, 400)
    response_page = browser.click_post_register_unsuccessful()
    assert response_page == response_api


def test_click_post_login_successful(browser, user_client):
    data = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response_api = user_client.post(APIRoutes.LOGIN, data, 200)
    response_page = browser.click_post_login_successful()
    assert response_page == response_api


def test_click_post_login_unsuccessful(browser, user_client):
    data = {"email": "peter@klaven"}
    response_api = user_client.post(APIRoutes.LOGIN, data, 400)
    response_page = browser.click_post_login_unsuccessful()
    assert response_page == response_api


def test_click_get_delay(browser, user_client):
    response_api = user_client.get(APIRoutes.DELAYED_RESPONSE)
    response_page = browser.click_get_delay()
    assert response_page == response_api
