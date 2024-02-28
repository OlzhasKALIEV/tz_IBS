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
    response = user_client.get(APIRoutes.USERS + id_user, 404)
    assert not response, "Expected response to be empty ({}), but received: {}".format({}, response)


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
    response = user_client.get(APIRoutes.SINGLE_RESOURCE + id_unknown, 404)
    assert not response, "Expected response to be empty ({}), but received: {}".format({}, response)


@pytest.mark.parametrize(
    "name, job",
    [
        (
                "morpheus",
                "leader",
        ),
        ("neo", "hacker"),
        ("trinity", "warrior"),
        ("morpheus", "developer"),
    ],
)
def test_post_create(user_client, name, job):
    data = {"name": name, "job": job}
    response = user_client.post(APIRoutes.USERS, data)
    assert response["name"] == name
    assert response["job"] == job


@pytest.mark.parametrize(
    "name, job, id_user",
    [
        ("morpheus", "leader", "2"),
        ("neo", "hacker", "5"),
        ("trinity", "warrior", "10"),
        ("morpheus", "developer", "100"),
    ],
)
def test_put_update(user_client, name, job, id_user):
    data = {"name": name, "job": job}
    response = user_client.put(APIRoutes.USERS + id_user, data)
    assert response["name"] == name
    assert response["job"] == job


@pytest.mark.parametrize(
    "name, job, id_user",
    [
        ("morpheus", "leader", "2"),
        ("neo", "hacker", "5"),
        ("trinity", "warrior", "10"),
        ("morpheus", "developer", "100"),
    ],
)
def test_patch_update(user_client, name, job, id_user):
    data = {"name": name, "job": job}
    response = user_client.patch(APIRoutes.USERS + id_user, data)
    assert response["name"] == name
    assert response["job"] == job


@pytest.mark.parametrize("id_user", ["1", "2", "5", "10"])
def test_delete_users(user_client, id_user):
    response = user_client.delete(APIRoutes.USERS + id_user)
    assert response is None


@pytest.mark.parametrize(
    "email, password",
    [
        ("george.bluth@reqres.in", "test_password_one"),
        ("janet.weaver@reqres.in", "test_password_two"),
        ("emma.wong@reqres.in", "test_password_three"),
        ("charles.morris@reqres.in", "test_password_four"),
    ],
)
def test_post_register(user_client, email, password):
    data = {"email": email, "password": password}
    response = user_client.post(APIRoutes.REGISTER, data, 200)
    assert "token" in response
    assert "id" in response


@pytest.mark.parametrize(
    "email",
    [
        "george.bluth@reqres.in",
        "janet.weaver@reqres.in",
        "emma.wong@reqres.in",
        "charles.morris@reqres.in",
    ],
)
def test_post_register_error(user_client, email):
    data = {"email": email}
    with pytest.raises(AssertionError, match="400"):
        user_client.post(APIRoutes.REGISTER, data)


@pytest.mark.parametrize(
    "email, password",
    [
        ("george.bluth@reqres.in", "test_password_one"),
        ("janet.weaver@reqres.in", "test_password_two"),
        ("emma.wong@reqres.in", "test_password_three"),
        ("charles.morris@reqres.in", "test_password_four"),
    ],
)
def test_post_login(user_client, email, password):
    data = {"email": email, "password": password}
    response = user_client.post(APIRoutes.LOGIN, data, 200)
    assert "token" in response


@pytest.mark.parametrize(
    "email",
    [
        "george.bluth@reqres.in",
        "janet.weaver@reqres.in",
        "emma.wong@reqres.in",
        "charles.morris@reqres.in",
    ],
)
def test_post_login_error(user_client, email):
    data = {"email": email}
    response = user_client.post(APIRoutes.LOGIN, data, 400)
    assert response['error'] == 'Missing password'


def test_get_delay(user_client):
    response = user_client.get(APIRoutes.DELAYED_RESPONSE)
    assert response['support']['text'] == 'To keep ReqRes free, contributions towards server costs are appreciated!'