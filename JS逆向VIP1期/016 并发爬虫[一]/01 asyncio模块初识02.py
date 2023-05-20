import asyncio
import time


async def task(i):  # 协程任务
    print(f"任务{i}启动")
    await asyncio.sleep(i)  # 异步任务
    print(f"任务{i}结束")


start = time.time()
# 创建事件循环对象
loop = asyncio.new_event_loop()
# 创建任务列表
tasks = [task(1), task(2)]  # 协程对象
print("tasks[0]",tasks[0])
loop.run_until_complete(asyncio.wait(tasks))  # 阻塞等待所有协程结束  # asyncio.wait 收集任务
print("cost timer:", time.time() - start)
