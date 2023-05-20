# yield : 迭代器和生成器: 优化存储
# yield : 实现协程

def get_data():
    for i in range(1,100):
        yield i


gen = get_data()  # <generator object get_data at 0x000002313B5F8AC0>

for i in gen:
    print(i)

# 生成器对象 以时间换空间
