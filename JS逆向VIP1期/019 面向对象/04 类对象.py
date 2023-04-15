# 声明类 : 类对象
class Student(object):

    class_name = "10"
    class_num = 500

    def __init__(self,name):
        self.name = name

    def listen(self):
        print(f"{self.name}听课")


s1 = Student("Jack")
s1.class_num = 600
s2 = Student("Jack")

# 针对类变量的修改,类对象与实例对象的区别: 实例对象无法更改类变量  实际原因是不在一个地址空间
print(Student.class_num) # 500
