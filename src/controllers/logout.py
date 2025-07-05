from flask import  make_response

def logout():

    res = make_response('Logged out')

    res.set_cookie("EXAMPLE_JWT_COOKIE", "")

    return res
