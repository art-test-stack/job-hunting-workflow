import os, pytest, httpx
from dotenv import load_dotenv

load_dotenv(".env.test")

AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
CLIENT_ID = os.getenv("AUTH0_CLIENT_ID")
CLIENT_SECRET = os.getenv("AUTH0_CLIENT_SECRET")
AUDIENCE = os.getenv("AUTH0_AUDIENCE")
USERNAME = os.getenv("AUTH0_TEST_USERNAME")
PASSWORD = os.getenv("AUTH0_TEST_PASSWORD")
BACKEND_URL = "http://localhost:8000"

@pytest.mark.asyncio
async def test_auth0_login_and_backend():
    async with httpx.AsyncClient() as client:
        token_resp = await client.post(
            f"https://{AUTH0_DOMAIN}/oauth/token",
            json={
                "grant_type": "password",
                "username": USERNAME,
                "password": PASSWORD,
                "audience": AUDIENCE,
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "scope": "openid profile email"
            }
        )
        token_resp.raise_for_status()
        token_data = token_resp.json()
        access_token = token_data["access_token"]

        resp = await client.get(
            f"{BACKEND_URL}/profile",
            headers={"Authorization": f"Bearer {access_token}"}
        )

        assert resp.status_code == 200
        data = resp.json()
        print("Authenticated user:", data)
        assert "user_id" in data
