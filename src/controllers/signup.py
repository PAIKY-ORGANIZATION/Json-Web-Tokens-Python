from typing import Any
from typing import cast
from flask import request as req, make_response
from src.db.db_init import User, get_session
from src.api_types import SignupRequest
from src.validators.validate_signup import validate_signup_body
from src.jwt.generate_token import generate_token


def signup():
    body: SignupRequest = req.get_json()
    username = body["unique_username"]
    food = body["favorite_food"]

    #* Validate and optionally return error
    error = validate_body(username, food)
    if error: return error

    #* Save and optionally return error
    result = save_to_db(username, food)
    if isinstance(result, tuple):  #% (error, status_code)
        return result # type: ignore

    user_id = result
    res = make_response("Success")
    generate_token(user_id=user_id, res=res)
    return res




def validate_body(username: Any, food: Any):
    result = validate_signup_body(username, food) #% Returns something like {"status": True, "message": "Success"}
    if not result["status"]:
        return result["message"], 400


def save_to_db(username: Any, food: Any):
    session = get_session()

    if session.query(User).filter_by(username=username).first():
        return "User already exists", 400

    user = User(username=username, favorite_food=food)
    session.add(user)
    session.commit()
    session.refresh(user)  # Ensure all generated fields are populated

    user_id = cast(int, user.user_id) # Don't return the column, returned the integer.

    return user_id
