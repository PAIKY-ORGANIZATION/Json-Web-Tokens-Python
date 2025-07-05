import os
from  flask import Response
import jwt


def generate_token(user_id: int, res: Response):
    secret = os.environ.get("JWT_SECRET")
    payload = {
        "userId": user_id
        # no "exp"
    }

    token = jwt.encode(payload, secret, algorithm="HS256") #type: ignore
    

    res.set_cookie("EXAMPLE_JWT_COOKIE", token, httponly=True)
    return token