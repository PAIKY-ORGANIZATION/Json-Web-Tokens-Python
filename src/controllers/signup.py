from flask import request as req
from src.db.db_init import User, get_session
from src.api_types import SignupRequest
from src.validators.validate_signup import validate_signup_body
from typing import Any


def signup():
    body: SignupRequest = req.get_json()
    username = body["unique_username"]
    food = body["favorite_food"]

    #* Validate and optionally return error
    error = validate_body(username, food)
    if error: return error

    #* Save and optionally return error
    error = save_to_db(username, food)
    if error: return error

    return "Success"


def validate_body(username: Any, food: Any):
    result = validate_signup_body(username, food) #% Returns something like {"status": True, "message": "Success"}
    if not result["status"]:
        return result["message"], 400


def save_to_db(username: Any, food: Any):
    session = get_session()

    if session.query(User).filter_by(username=username).first():
        return "User already exists", 400

    session.add(User(username=username, favorite_food=food))
    session.commit()
    session.close()
