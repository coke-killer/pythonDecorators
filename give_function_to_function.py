# __author__: "Yu Dongyue"
# date: 2021/5/8
# 将函数作为参数传给另一个函数
def hi():
    return 'hi Hwang'


def doSomeThingBeforeHi(func):
    print('i am doing some funny work before executing hi()')
    print(func())
    print('i am doing some funny work after executing hi()')


doSomeThingBeforeHi(hi)
# 装饰器让你在一个函数的前后去执行代码,oho,像极了aop
