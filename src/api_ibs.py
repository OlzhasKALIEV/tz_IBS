import json

import requests


class ApiIBS:
    """
    Класс для взаимодействия с API.
    """

    def __init__(self, settings):
        """
        Инициализация клиента API.

        :param settings: Настройки клиента.
        """
        self.settings = settings
        self.session = requests.session()

    def __base_call(self, method: str, url: str, status_code: int, data: dict = None):
        url = self.settings.base_url + url
        response = self.session.request(method, url, json=data)
        assert response.status_code == status_code, f"{response.status_code}"
        try:
            return response.json()
        except json.decoder.JSONDecodeError:
            return None

    def get(self, url: str, status_code: int = 200):
        """
        Метод для выполнения GET-запроса.
            :param url: Конечная точка API.
            :param status_code: Ожидаемый HTTP-статус код.
            :return: Ответ API в формате JSON.

        """
        return self.__base_call("get", url, status_code=status_code)

    def post(self, url: str, data: dict = None, status_code: int = 201):
        """
        Метод для выполнения POST-запроса.

            :param url: Конечная точка API.
            :param data: Данные запроса. {"name": "morpheus","job": "leader"}
            :param status_code: Ожидаемый HTTP-статус код.
            :return: Ответ API в формате JSON.

        """
        return self.__base_call("post", url, data=data, status_code=status_code)

    def put(self, url: str, data: [dict, list], status_code: int = 200):
        """
        Метод для выполнения PUT-запроса.

            :param url: Конечная точка API.
            :param data: Данные запроса. {"name": "morpheus","job": "zion resident"}
            :param status_code: Ожидаемый HTTP-статус код.
            :return: Ответ API в формате JSON.

        """
        return self.__base_call("put", url, data=data, status_code=status_code)

    def patch(self, url: str, data: [dict, list], status_code: int = 200):
        """
        Метод для выполнения PATCH-запроса.

            :param url: Конечная точка API.
            :param data: Данные запроса. {"name": "morpheus","job": "zion resident"}
            :param status_code: Ожидаемый HTTP-статус код.
            :return: Ответ API в формате JSON.

        """
        return self.__base_call("patch", url, data=data, status_code=status_code)

    def delete(self, url: str, status_code: int = 204):
        """
        Метод для выполнения DELETE-запроса.

            :param url: Конечная точка API.
            :param status_code: Ожидаемый HTTP-статус код.

        """
        return self.__base_call("delete", url, status_code=status_code)
