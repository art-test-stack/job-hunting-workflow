from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    auth0_domain: str
    auth0_audience: str
    auth0_client_id: str
    auth0_client_secret: str
    algorithms: list[str] = ["RS256"]
    environment: str = "development"

    db_url: str = f"sqlite:///database.db"

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
