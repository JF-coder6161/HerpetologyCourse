# 标识字符串可以用双引号，也可以用单引号
name = "yuan"
name = 'rain'

# （1）字符串的转义符号 : \
# 转义符号： \ 的功能有两个
# 1.赋予一些普通符号以特殊功能
# 2.取消一些特殊符号的特殊功能变为普通符号

# \n 换行符
print("Hello world\nHello yuan")
print("Hello world \\ Hello yuan")
print('i\'am yuan')

# 格式化输出
name = "yuan"
age = 18
# 模板
print("我的姓名:%s,我的年龄:%s" % (name, age))

print(f"我的姓名:{name},我的年龄:{age}")

# 序列类型操作
s = "hello yuan"
# 索引操作 获取一个字符 字符串[索引]
print(s[8])
print(s[-2])
# 切片操作： 获取一段字符串  字符串[开始索引:结束索引:步长=1] 前闭后开
print(s[6:])

# in 操作  判断是否存在
print('yuan' in s) # True
print('yuan ' in s) # False

# + 拼接
a = "Hello"
b = "yuan"
print(a + b) # Helloyuan