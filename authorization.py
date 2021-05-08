# __author__: "Yu Dongyue"
# date: 2021/5/8
# 装饰器使用场景授权，装饰器有助于检查某个人是否被授权去使用一个web应用断电，它们被大量使用于Flash和Django框架中
from functools import wraps


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authenticate()
        return f(*args, **kwargs)

    return decorated
