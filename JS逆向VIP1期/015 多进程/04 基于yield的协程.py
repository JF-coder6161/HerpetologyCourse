# 实现协程并发

def foo():
    print("foo start")

    yield

    print("foo end")

    yield


def bar():
    print("bar start")

    yield

    print("bar end")

    yield


gen_foo = foo()  # 生成器对象
gen_bar = bar()

next(gen_foo)
next(gen_bar)
next(gen_foo)
next(gen_bar)
