import os  #

# 1.创建文件夹
# os.mkdir("我的模块")


# 2.路径拼接

with open("我的模块/abc.txt", "w") as f:
    pass

print(os.path.sep)  # 路径分隔符 \

path = os.path.join("我的模块", "apple.txt")
print(path) # 我的模块\apple.txt

# 3.获取文件或文件夹的目录
print(os.path.dirname(__file__)) # F:\PyCharmProject\HerpetologyCourse\JS逆向VIP1期\012 Requests应用案例
print(os.path.dirname(path)) # 我的模块


# 4. exists 判断是否存在某文件或目录

print(os.path.exists("我的模块"))

# 5. basename 获取指定路径的基本名称
print(os.path.basename(path)) # apple.txt

# split 分割路径
print(os.path.split(path)) # ('我的模块', 'apple.txt')