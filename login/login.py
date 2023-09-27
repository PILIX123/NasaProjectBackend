import requests
import hvac
import dotenv
import os

class Login():
    def login(self):
        dotenv.load_dotenv("./vaultconfig/.env")
        client=hvac.Client(url="http://192.168.2.19:8200",token=os.getenv("VAULTTOKEN"))

        read_response=client.secrets.kv.read_secret_version(path="nasa")
        keyValue=read_response['data']['data']['api']

        print(keyValue)