from typing import Any, Dict, TypeAlias



Validate_returned_type: TypeAlias = Dict[str, bool | str]

def validate_signup_body(unique_username: Any, favorite_food: Any) -> Validate_returned_type:
    if(not unique_username or not isinstance(unique_username, str)):
        return {"status":  False, "message": "invalid username"}
    
    if(not favorite_food or not isinstance(favorite_food, str)):
        return {"status":  False, "message": "invalid favorite food"}

    return {"status": True, "message": "Success"}
