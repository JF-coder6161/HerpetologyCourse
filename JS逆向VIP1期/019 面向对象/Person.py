class Person:
    # 类属性
    legs_num = 2
    has_emotion = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def play_fire(self):

        print("%s玩火"%self.name)


# 实例对象和类对象可以获取类属性，但是只有类对象才能修改类属性
yuan = Person("yuan", 18)
alvin = Person("alvin", 18)

print(yuan.legs_num)
print(yuan.name)
# Person：一个类对象
print(Person.legs_num)
Person.legs_num = 3
print(Person.legs_num)
yuan.legs_num = 4
print(Person.legs_num)