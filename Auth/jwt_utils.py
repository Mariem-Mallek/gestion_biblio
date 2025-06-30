import jwt
from chalice import UnauthorizedError

SECRET_KEY = "clé_GESTION_biblio"


def require_auth(request):
    token = request.headers.get("Authorization")
    if not token:
        raise UnauthorizedError("Token manquant")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        raise UnauthorizedError("Token expiré")
    except jwt.InvalidTokenError:
        raise UnauthorizedError("Token invalide")
