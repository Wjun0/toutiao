from flask import request, g
from .jwt_utils import verify_jwt

def get_userinfo():
    header = request.headers.get('Authorization')
    g.userid = None

    if header and header.startswith('Bearer'):
        token = header[7:]

        #校验jwt
        payload = verify_jwt(token)
        if payload:
            g.userid = payload.get('userid')


