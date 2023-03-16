# 变量的作用域 ， 变量的声明周期
age = 100  # 全局变量


def bar():
    global age  # 局部变量想应用全局变量 加 global
    age = 10  # 即 bar.age

    print("bar x", age)


bar()
print(age)  # 10
