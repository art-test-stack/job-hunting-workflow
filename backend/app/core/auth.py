from jose import jwt
from jose.exceptions import JWTError
from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPBearer
import httpx
import os
from app.core.config import settings

security = HTTPBearer()

async def get_jwk():
    url = f"https://{settings.auth0_domain}/.well-known/jwks.json"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
    resp.raise_for_status()
    return resp.json()

async def verify_token(token: str = Security(security)):
    token = token.credentials
    jwks = await get_jwk()
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = next(
        (
            {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"],
            }
            for key in jwks["keys"]
            if key["kid"] == unverified_header["kid"]
        ),
        None,
    )
    if not rsa_key:
        raise HTTPException(status_code=401, detail="Invalid header")
    try:
        payload = jwt.decode(
            token,
            rsa_key,
            algorithms=settings.algorithms,
            # audience="https://job-tracker.eu.auth0.com/userinfo",
            audience=settings.auth0_audience,
            issuer=f"https://{settings.auth0_domain}/"
        )
    except JWTError as e:
        raise HTTPException(status_code=401, detail=str(e))
    return payload  # Contains user info (sub, email if included, etc.)


async def get_user_info(user_id: str):
    async with httpx.AsyncClient() as client:
        data = {
            "grant_type": "client_credentials",
            "client_id": settings.auth0_client_id,
            "client_secret": settings.auth0_client_secret,
            "audience": settings.auth0_audience
            # "audience": f"https://{settings.auth0_domain}/api/userinfo"
        }
        token_resp = await client.post(f"https://{settings.auth0_domain}/oauth/token", json=data)
        token_resp.raise_for_status()
        mgmt_token = token_resp.json()["access_token"]

        # Call the Management API
        headers = {"Authorization": f"Bearer {mgmt_token}"}
        user_resp = await client.get(
            f"https://{settings.auth0_domain}/api/v2/users/{user_id}",
            headers=headers
        )
        user_resp.raise_for_status()
        return user_resp.json()
