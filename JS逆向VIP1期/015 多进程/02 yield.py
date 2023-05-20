# yield : 迭代器和生成器: 优化存储

list = [1, 2, 3]


def get_data():
    print("Start")
    yield 1  # 暂时返回保存状态
    print("come back")
    yield 2
    print("come back 2")
    yield 3


gen = get_data()  # <generator object get_data at 0x000002313B5F8AC0>
print(gen)

# gen.send(None)
ret= next(gen)
print(ret)
