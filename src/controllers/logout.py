from flask import  make_response, jsonify

def logout():

    res = make_response(jsonify({
        "message": "Logged out successful",
        "success": True
    }))

    res.set_cookie("EXAMPLE_JWT_COOKIE", "")

    return res
