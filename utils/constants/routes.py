from enum import Enum


class APIRoutes(str, Enum):
    LIST_USERS = '/api/users?page='
    USERS = '/api/users/'
    RESOURCE = '/api/unknown/'
    REGISTER = '/api/register'
    LOGIN = '/api/login'
    DELAYED_RESPONSE = '/api/users?delay='

    def __str__(self) -> str:
        return self.value
