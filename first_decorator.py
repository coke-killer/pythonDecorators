# __author__: "Yu Dongyue"
# date: 2021/5/8
from functools import wraps


def a_new_decorator(a_func):
    def wrapTheFunction():
        print('i am doing some funny work before executing hi()')
        a_func()
        print('i am doing some funny work after executing hi()')

    return wrapTheFunction


@a_new_decorator
def a_function_requiring_decoration():
    print('i am the function which needs some decoration to remove mo foul smell')


a_function_requiring_decoration()
# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
# a_function_requiring_decoration()
print(a_function_requiring_decoration.__name__)


# 上面的例子显示a_function_requiring_decoration这个函数被wrapTheFunction这个函数替代了

def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print('i am doing some funny work before executing hi()')
        a_func()
        print('i am doing some funny work after executing hi()')

    return wrapTheFunction


@a_new_decorator
def a_function_requiring_decoration():
    """Hey yo! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")


print(a_function_requiring_decoration.__name__)
if __name__ == '__main__':
    a_function_requiring_decoration()
