from vaultpy.vault import Vault
from fastapi import FastAPI
import requests
import json

app = FastAPI(title="Backend Nasa", docs_url="/nasa/docs",
              openapi_url="/power/docs/openapi.json")

vault = Vault()

@app.get("/nasa/apod",summary="Get the picture of the day and some other data")
async def get_apod():
    data = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={vault.get_nasa_key()}")
    data.close()
    data = json.loads(data.content.decode())
    return data