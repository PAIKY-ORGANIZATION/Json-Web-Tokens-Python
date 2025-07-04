from src.app_setup import app
from src.controllers.signup import signup


@app.post('/api/signup')

def endpoint_signup():
    return signup()