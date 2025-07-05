from flask import request as req
from src.db.db_init import User, get_session
from src.api_types import SignupRequest
from src.validators.validate_signup import validate_signup_body

def signup():

    body: SignupRequest = req.get_json()

    unique_username = body["unique_username"]
    favorite_food = body["favorite_food"]


    result = validate_signup_body(unique_username=unique_username, favorite_food=favorite_food)
    status = result["status"]    
    message = result["message"]    

    print(status, message)

    session = get_session()



    #* Check if the user already exists.
    saved = session.query(User).filter(User.username == unique_username).first()
    if saved: return "User already exitss"

    #* Create and save the user
    new_user = User(username=unique_username, favorite_food=favorite_food)
    session.add(new_user)
    session.commit()
    

    save_users = session.query(User).all() 
    session.close()
    for user in save_users:
        print(user)
    return "Success"