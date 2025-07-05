from typing import Any
from typing import cast
from flask import request as req, make_response, jsonify
from werkzeug.exceptions import BadRequest
from src.db.db_init import User, get_session
# from src.api_types import SignupRequest
from src.validators.validate_signup import validate_signup_body
from src.jwt.generate_token import generate_token

def signup():
    body = req.get_json(silent=True)
    if not isinstance(body, dict):
        return jsonify({"error": "Invalid or missing JSON"}), 400

    username = body.get("unique_username")
    food = body.get("favorite_food")

    if not isinstance(username, str) or not isinstance(food, str):
        return jsonify({"error": "Invalid types"}), 400

    validation = validate_signup_body(username, food)
    if not validation["status"]:
        return jsonify({"error": validation["message"]}), 400

    result = save_to_db(username, food)
    if isinstance(result, tuple):
        return jsonify({"error": result[0]}), result[1]

    user_id = result
    res = make_response("Success")
    generate_token(user_id=user_id, res=res)
    return res



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
