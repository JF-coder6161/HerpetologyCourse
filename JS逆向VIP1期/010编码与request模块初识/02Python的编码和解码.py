

s = "i am 仅"

# 编码方法
ret1 = s.encode(encoding="utf-8")
ret2 = s.encode(encoding="GBK")

# 解码方法 字节数据对象 decode("规则")  python3 默认编码格式为utf-8
ret1.decode(encoding="utf-8")
ret2.decode(encoding="gbk")

# 存储 依赖字节
# 网络 依赖字节


