from src.app_setup import app
from src.controllers.signup import signup
from src.controllers.get_saved_session import get_saved_session

@app.post('/api/signup') #type:  ignore

def endpoint_signup():
    return signup()

@app.get('/api/get-saved-session')
def endpoint_get_saved_session():
    return get_saved_session()

@app.delete('/api/delete-session')
def endpoint_delete_session():
    return 'Test - Success'