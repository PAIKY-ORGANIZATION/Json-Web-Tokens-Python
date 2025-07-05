from typing import Any
import os
from flask import request as res
import jwt
from jwt import InvalidTokenError


def verify_token() -> tuple[Any, Any, Any]:
    token = res.cookies.get("EXAMPLE_JWT_COOKIE")
    if not token:
        return None, "Missing token", 401
    
    try:
        secret = os.environ.get("JWT_SECRET")
        payload: dict[str, Any] = jwt.decode(token, secret, algorithms=["HS256"]) # type: ignore
        return payload, None, None
    except InvalidTokenError:
        return None, "Invalid token", 401