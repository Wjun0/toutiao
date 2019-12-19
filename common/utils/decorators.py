from functools import wraps

from flask import g, abort


def login_required(f):
    @wraps(f)
    def wrapper(*args,**kwargs):
        if g.userid:
            return f(*args,**kwargs)
        else:
            abort(401)

    return wrapper
