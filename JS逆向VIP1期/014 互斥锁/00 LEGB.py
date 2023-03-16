# 变量的作用域 ， 变量的声明周期
x =100 # 全局变量

def foo():
    y = 20 # 局部变量
    print(x)

foo()

# print(y)

# 函数内部变量 -> 全局变量 -> 内建变量
# LEGB local(局部变量) --> enclosing(嵌套变量) --> global(全局变量) --> builtin(内建变量)

y = 100

def foo1():
    print("foo1")
    y = 10
    def bar1():
        y = 1
        print("bar1",y)

    bar1()

foo1()

