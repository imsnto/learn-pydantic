from pydantic_settings import BaseSettings

# Setting Management
class Settings(BaseSettings):
    API_KEY : str
    DEBUG : bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
print(f"API KEY : {settings.API_KEY}")
print(f"Type of DEBUG : {type(settings.DEBUG)}")