import pytest

from utils.constants.routes import APIRoutes


@pytest.mark.parametrize("page", ["1", "2", "5", "10", "100"])
def test_get_list_users(user_client, page):
    response = user_client.get(APIRoutes.LIST_USERS + page)
    assert response["page"] == int(page)


@pytest.mark.parametrize("id_user", ["1", "2", "5", "10"])
def test_get_single_user(user_client, id_user):
    response = user_client.get(APIRoutes.USERS + id_user)
    assert response["data"]["id"] == int(id_user)


@pytest.mark.parametrize("id_user", ["0", "23"])
def test_get_single_user_error(user_client, id_user):
    with pytest.raises(AssertionError, match="404"):
        response = user_client.get(APIRoutes.USERS + id_user)
        assert response.status_code == 404


@pytest.mark.parametrize("page", ["1", "2", "5", "10", "100"])
def test_get_list_resource(user_client, page):
    response = user_client.get(APIRoutes.LIST_RESOURCE + page)
    assert response["page"] == int(page)


@pytest.mark.parametrize("id_unknown", ["2", "5", "10"])
def test_get_single_resource(user_client, id_unknown):
    response = user_client.get(APIRoutes.SINGLE_RESOURCE + id_unknown)
    assert response["data"]["id"] == int(id_unknown)


@pytest.mark.parametrize("id_unknown", ["0", "23"])
def test_get_single_resource_error(user_client, id_unknown):
    with pytest.raises(AssertionError, match="404"):
        response = user_client.get(APIRoutes.SINGLE_RESOURCE + id_unknown)
        assert response.status_code == 404


@pytest.mark.parametrize(
    "name, job", [("morpheus", "leader"), ("neo", "hacker"), ("trinity", "warrior")]
)
def test_post_create(user_client, name, job):
    data = {"name": name, "job": job}
    response = user_client.post(APIRoutes.USERS, data)
    assert response["name"] == name
    assert response["job"] == job
