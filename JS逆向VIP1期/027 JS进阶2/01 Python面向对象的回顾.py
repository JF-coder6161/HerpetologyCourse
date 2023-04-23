# 类与对象
# 实例对象, 类对象
# 实例变量(实例属性), 类变量(类属性,类成员变量)
# 实例方法, 类方法 , 静态方法

class Person(object):
    data = ""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法
    def read(self):
        print(self.name + "reading")

    def listen(self):
        print(self.name + "listening")

    def foo(self):
        pass
