# __author__: "Yu Dongyue"
# date: 2021/5/8
def hi(name="yes"):
    return "hi" + name


print(hi())

# 将函数赋值给一个变量
greet = hi
print(greet)
# 删除旧的hi函数，看看发生什么
del hi
print(hi())
print(greet)
