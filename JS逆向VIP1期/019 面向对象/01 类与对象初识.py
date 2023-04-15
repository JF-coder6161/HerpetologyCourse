'''
代码的组织类型  :  包 -> 模块 -> 类 -> 函数
prop = []
lifeValue = 100


def attack():
    global lifeValue
    print("attack,go go go")
    lifeValue -= 1
类 : 函数 + 数据
'''

# 声明类
class Person(object):

    # 类属性
    isMotion = True
    legs = 2
    hasLanguage = True

    # 实例方法
    def eat(self):
        print("eating ...")

    def sleep(self):
        print("sleep ...")

    def run(self):
        print("run ...")

# 实例化
p1 = Person()
# 实例化对象调用属性和方法通过句点符号
print(p1.legs)
print(p1.eat())