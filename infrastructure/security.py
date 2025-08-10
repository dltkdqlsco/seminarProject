import jwt
import datetime

class Security:
    @staticmethod
    def create_token(user_id, role, secret, expires_in=3600):
        payload = {
            'sub': user_id,
            'role': role,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_in),
            'iat': datetime.datetime.utcnow()
        }
        return jwt.encode(payload, secret, algorithm='HS256')

    @staticmethod
    def decode_token(token, secret):
        try:
            return jwt.decode(token, secret, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise PermissionError("Token expired")
        except Exception:
            raise PermissionError("Invalid token")
