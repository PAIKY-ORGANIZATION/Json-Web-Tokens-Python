from src.app_setup import app
from src.controllers.signup import signup


@app.post('/api/signup')

def endpoint_signup():
    return signup()

@app.get('/api/get-saved-session')
def endpoint_get_saved_session():
    return 'Test - Success'

@app.delete('/api/delete-session')
def endpoint_delete_session():
    return 'Test - Success'