from typing import Any, Dict





def validate_signup_body(unique_username: Any, favorite_food: str | None) -> :
    if(not unique_username or not isinstance(unique_username, str)):
        return {"status":  False, "message": "invalid username"}
