import asyncio
import time



async def foo(i):  # 协程任务
    print(f"任务{i}启动")
    await asyncio.sleep(i)  # 异步任务
    print(f"任务{i}结束")
    return i * i

def callTask2Back(ret):
    print("异步任务2结果",ret.result())

start = time.time()
# 1.创建事件循环对象
loop = asyncio.get_event_loop()
# 2.创建任务对象列表
tasks = [
    asyncio.ensure_future(foo(1)),
    asyncio.ensure_future(foo(2)),
    asyncio.ensure_future(foo(3)),
    ] # task(1) asyncio.Task

tasks[1].add_done_callback(callTask2Back) # 回调函数 运行完成后立刻返回

# 3.启动协程
loop.run_until_complete( asyncio.wait(tasks))  # 阻塞等待所有协程结束  # asyncio.wait 收集任务

print(tasks[0])
print(tasks[0].done()) # 布尔值 是否返回结果
print(tasks[0].result()) # 返回结果
print("cost timer:", time.time() - start)

res = []
for i in tasks:
    res.append(i.result())

print(res)