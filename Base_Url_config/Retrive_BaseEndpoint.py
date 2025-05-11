import requests
from pathlib import Path
import json


class Accessing_baseurl:
    CONFIG_PATH = Path(r"D:\MyPythonProjects\API Automation\Endpoints Config\config.json")

    @staticmethod
    def access_base_endpoint():
        try:
            with Accessing_baseurl.CONFIG_PATH.open() as json_file:
                file_content = json_file.read()
                properties = json.loads(file_content)
                env = properties["environment"]["env"]
                return properties[env]["base_url"]
        except(FileNotFoundError, KeyError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Failed to load base endpoint: {e}")

    @staticmethod
    def get_base_endpoint():
        base_url = Accessing_baseurl.access_base_endpoint()
        return base_url


obj = Accessing_baseurl()
obj.access_base_endpoint()
obj.get_base_endpoint()
