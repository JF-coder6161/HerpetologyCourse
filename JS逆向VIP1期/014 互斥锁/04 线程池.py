import time
from concurrent.futures import ThreadPoolExecutor


def task(i):
    print(f'任务{i}开始')
    time.sleep(i)
    print(f'任务{i}结束')
    return i


pool = ThreadPoolExecutor(3)

start = time.time()

future_list = []

for i in range(1, 4):
    # 线程池技术实现异步,完成并发
    ret = pool.submit(task, i)  # future对象(异步结果对象)
    # ret.result()
    # ret.done() # 返回boolean值 true -> 结果返回 false -> 结果未返回  即返回结果是否回写
    future_list.append(ret)

pool.shutdown()  # 线程阻塞

print(f"耗时{time.time() - start}秒")

print(
    future_list)  # [<Future at 0x13c2299d8b0 state=finished returned int>, <Future at 0x13c22a1a640 state=finished returned int>, <Future at 0x13c22a1a9d0 state=finished returned int>]

print([future.result() for future in future_list])  # [1.2.3]
