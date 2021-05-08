# __author__: "Yu Dongyue"
# date: 2021/5/8
# 从函数中返回函数、
def hi(name='Hwang'):
    def greet():
        return 'now youi are in the greet() function'

    def welcome():
        return 'now you are in the welcome() function'

    if name == 'Hwang':
        return greet
    else:
        return welcome


a = hi()
print(a)
# 上面结果显示 a现在指向hi()函数中的greet()函数

print(a())
# 在if/else语句中我们返回greet和welcome.而不是greet()和welcome(),是因为当你吧小括号放在后面，这个函数就会执行；不方括号，那它可以导出传递，并且可以赋值给别的变量而不去执行它。
# 当我们写下a=hi(),hi()会被执行，由于name参数默认是Hwang,所以greet被返回了。如果我们吧语句改为a=hi(name='ali),那么welcome函数将被返回，我们还可以打印出hi()()，这会输出now youi are in the greet() function
