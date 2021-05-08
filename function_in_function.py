# __author__: "Yu Dongyue"
# date: 2021/5/8
# 在函数中定义函数
def hi(name='hahaha'):
    print('now you are inside the hi() function')

    def greet():
        return 'now you are in the greet() function'

    def welcome():
        return 'now you are in the welcome() function'

    print(greet())
    print(welcome())
    print('now you are back in the hi() function')


hi()
# 上面展示了无论何时你调用hi(),greet()和welcome()将会被同时调用。
# 然后greet()和welcome()函数在hi()函数之外事不能被访问的，比如：
greet()
