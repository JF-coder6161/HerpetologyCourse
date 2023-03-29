import asyncio
import time

def task(i):
    print(f"任务{i}启动")
    time.sleep(i)
    print(f"任务{i}结束")


start = time.time()
task(1)
task(2)
print("cost timer:",time.time() - start)