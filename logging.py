# __author__: "Yu Dongyue"
# date: 2021/5/8
from functools import wraps


def login(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + "was called")
        return func(*args, **kwargs)

    return with_logging


@login
def addition_func(x):
    return x + x


if __name__ == '__main__':
    a = addition_func(4)
    print(a)
