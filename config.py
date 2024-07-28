import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    def __init__(self):
        self.app_name = os.getenv("APP_NAME", "Pokemon REST API")
        self.pokeapi_url = os.getenv("POKEAPI_URL", "https://pokeapi.co/api/v2")


settings = Settings()
