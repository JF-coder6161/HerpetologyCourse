import time

def task(i):
    print(f'任务{i}开始')
    time.sleep(i)
    print(f'任务{i}结束')
    return i