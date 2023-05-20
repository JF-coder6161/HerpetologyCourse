import multiprocessing
from multiprocessing import process

# process 拥有和 threading.Thread() 同样的API

import time

def foo(t):
    print(f"任务{t}开始")
    time.sleep(t)
    print(f"任务{t}结束")

if __name__ == '__main__':
    startTime = time.time()

    process_list = []
    for i in range(3):
        # 基于多进程的并发
        t1 = multiprocessing.Process(target=foo, args=(i,))
        t1.start()  # 调度进程对象
        process_list.append(t1)

    for process in process_list:
        process.join()

    print(f"耗时{time.time() - startTime}")




