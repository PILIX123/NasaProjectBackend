from vaultpy.vault import Vault
from fastapi import FastAPI


app = FastAPI(title="Backend Nasa", docs_url="/nasa/docs",
              openapi_url="/power/docs/openapi.json")

vault = Vault()

@app.get("/nasa/apod",summary="Get the picture of the day and some other data")
async def get_apod():