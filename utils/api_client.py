import requests
from requests import Response

class ApiClient:
    def __init__(self, base_url: str, api_key: str) -> None:
        self.base_url = base_url
        self.api_key = api_key


    def get(self, endpoint: str) -> Response:
        response = requests.get(
            url=self.base_url + endpoint,
            headers={"x-api-key": self.api_key}
        )

        return response


    def post(self, endpoint: str, body: dict | None = None) -> Response:
        response = requests.post(
            url=self.base_url + endpoint, 
            headers={"x-api-key": self.api_key},
            json=body
        )

        return response
    

    def put(self, endpoint: str, body: dict | None = None) -> Response:
        response = requests.put(
            url=self.base_url + endpoint,
            headers={"x-api-key": self.api_key},
            json=body
        )
    
        return response


    def delete(self, endpoint: str) -> Response:
        response = requests.delete(
            url=self.base_url + endpoint,
            headers={"x-api-key": self.api_key},
        )

        return response