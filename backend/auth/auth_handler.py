import time
from typing import Dict

import jwt
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


def token_response(token: str):
    return {"token": token}


def signJWT(user_id: str):
    payload = {"user_id": user_id, "expires": time.time()}

    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    #return token_response(token)
    return token

def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token
    except:
        return {}
