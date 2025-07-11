from typing import TypedDict, Any

class SignupRequest(TypedDict):
    unique_username: str
    favorite_food: str


class ServerResponse(TypedDict):
    message:  str
    success: bool
    data: Any