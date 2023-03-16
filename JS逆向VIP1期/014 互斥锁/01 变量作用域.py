# 变量的作用域 ， 变量的声明周期
x = 100  # 全局变量


def foo():
    print(x)


def bar():
    x = 10
    print("bar x", x)




foo()
bar()

