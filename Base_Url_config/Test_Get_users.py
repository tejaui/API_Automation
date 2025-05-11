import json
import pytest
import requests
from Retrive_BaseEndpoint import Accessing_baseurl


class Functional_Test:
    @staticmethod
    @pytest.mark.sanity
    def test_get_users():
        Invoke_baseurl = Accessing_baseurl.get_base_endpoint()
        url = f"{Invoke_baseurl}/public/v2/users"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer 55fccffdc197ff11a411e41489f23db315981ec45c67bb02cb55dca0d69880f9",
            "Accept": "application/json"
        }
        send_request = requests.get(url, headers=headers)
        response = send_request.json()
        print(response)


obj = Functional_Test
obj.test_get_users()
