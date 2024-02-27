import pytest

from utils.constants.routes import APIRoutes


@pytest.mark.parametrize("page", ["2", "5", "10"])
def test_get_list_users(user_client, page):
    response = user_client.get(APIRoutes.LIST_USERS + page)
    assert response["page"] == page
