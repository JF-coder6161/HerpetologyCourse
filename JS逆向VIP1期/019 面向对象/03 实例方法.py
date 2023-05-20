class Person(object):
    isMotion = True
    legs = 2
    hasLanguage = True

    def __init__(self, name, age, sex, weight):
        self.name = name
        self.age = age
        self.sex = sex
        self.weight = weight

    # 实例方法
    def eat(self):
        print(f"{self.name},eating ...")

    def sleep(self):
        print("sleep ...")

    # self 谁调用就是谁
    def run(self):
        print("run ...")


# 实例化
p1 = Person('jack', 12, 1, 11)
p1.eat() # jack,eating ...

p1.run = 100
p1.run() # TypeError: 'int' object is not callable   (实例空间找 run到了run  而不是找run()  )


