# with open("我的一天", mode="r",encoding = "GBK") as f: encoding = "GBK" 告诉操作系统解码用 "GBK"
with open("我的一天", mode="r", encoding="utf-8") as f:
    data = f.read()
print(data)

# f.read()  -->  f句柄通知操作系统 读取文件 , 操作系统读取文件并解码( windows操作系统 默认解码格式GBK linux mac utf-8)

with open("GBK", mode="r") as f1:
    data = f1.read()
print(data)

# 写操作 不指定encoding 按照系统默认编码进行编码写入文件
with open("写操作", mode="w") as f2:
    data = f.write("我的一天")


# rb 模式  读字节 (操作系统不进行解码，不需要encoding参数)
with open("GBK", mode="rb") as f1:
    data = f1.read().decode("utf-8") # decode("xx") python指定解码格式 读取文件 与操作系统无关
print(data)

# wb 模式  写字节 (操作系统不进行编码 不需要encoding参数)
with open("写操作", mode="w") as f2:
    data = f.write("我的一天".encode("utf-8")) # encode("xx") python指定编码格式 写入文件 与操作系统无关