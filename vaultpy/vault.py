import hvac
import dotenv
import os

class Vault():
    def __init__(self) -> None:
        dotenv.load_dotenv("./vaultconfig/.env")
        self.client = hvac.Client(url="http://192.168.2.19:8200",token=os.getenv("VAULTTOKEN"))
    def get_nasa_key(self)->str:
        read_response=self.client.secrets.kv.read_secret_version(path="nasa")
        keyValue=read_response['data']['data']['api']
        return keyValue