import jwt
import datetime
from Auth.jwt_utils import SECRET_KEY

def login(app):
    req = app.current_request
    body = req.json_body
    username = body.get("username")
    password = body.get("password")

    if username == "admin" and password == "admin123":
        payload = {
            "user": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return {"token": token}
    else:
        return {"error": "Invalid credentials"}, 401
