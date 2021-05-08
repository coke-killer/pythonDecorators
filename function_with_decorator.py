# __author__: "Yu Dongyue"
# date: 2021/5/8
# 带参数的装饰器
from functools import wraps


def log(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + 'was called'
            print(log_string)
            # 打开logfile，并写入内容
            with open(logfile, 'a') as opened_file:
                # 现在将日志打到指定的logfile
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)

        return wrapped_function

    return logging_decorator


@log(logfile='func2.log')
def my_func1():
    pass


if __name__ == '__main__':
    my_func1()
