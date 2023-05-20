# # 声明类 : 类对象
# # 版本2 静态方法
# class Student(object):
#     cls_number = 500
#
#     @staticmethod
#     def show_class_num():
#         print(Student.cls_number)
#
#     @staticmethod
#     def add_class_num():
#         Student.cls_number += 1
#
#
# Student.show_class_num()
# Student.add_class_num()
# Student.show_class_num()


# 声明类 : 类对象
# 版本3 类方法
class Student(object):
    cls_number = 500

    @classmethod
    def show_class_num(cls):
        print(id(cls))
        print(cls.cls_number)

    @classmethod
    def add_class_num(cls):
        cls.cls_number += 1


print(id(Student))
Student.show_class_num()

Student.add_class_num()
Student.show_class_num()
