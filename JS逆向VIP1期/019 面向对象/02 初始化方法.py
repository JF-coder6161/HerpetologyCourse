class Person(object):
    # 类属性
    isMotion = True
    legs = 2
    hasLanguage = True

    def __init__(self, name, age, sex, weight):
        '''
        实例属性或实例变量
        :param name:
        :param age:
        :param sex:
        :param weight:
        '''
        print("self:::", id(self))
        self.name = name
        self.age = age
        self.sex = sex
        self.weight = weight

    # 实例方法
    def eat(self):
        print("eating ...")

    def sleep(self):
        print("sleep ...")

    def run(self):
        print("run ...")


# 实例化
p1 = Person('jack', 12, 1, 11)
# 实例化对象调用属性和方法通过句点符号
print("p1:::", id(p1))

p2 = Person('jack', 12, 1, 11)
# 实例化对象调用属性和方法通过句点符号
print("p1:::", id(p2))
