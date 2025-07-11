from flask import jsonify
from src.jwt.verify_token import verify_token
from src.db.db_init import get_session, User

def get_saved_session():
    payload, error_msg = verify_token()
    if error_msg:
        return jsonify({"message": error_msg, "success": False}), 400
    

    user = get_user_by_id(payload["userId"])
    if not user:
        return jsonify({"message": "User not found", "success": False}), 400

    return "Session found, your favorite food is: " + user.favorite_food


def get_user_by_id(user_id: str):
    session = get_session()
    return session.query(User).filter_by(user_id=user_id).first()
