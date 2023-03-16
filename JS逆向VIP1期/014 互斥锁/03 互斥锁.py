import threading
import time

# 时间片 上限 10ms 左右

lock = threading.Lock()
# # 加锁
# lock.acquire()
# # 释放锁
# lock.release()

x = 1000


def sub():
    # 加锁
    #lock.acquire()
    global x
    temp = x - 1
    time.sleep(0.1)
    x = temp
    # 释放锁
    #lock.release()


# 串行版本
# for i in range(100):
#     sub()
#
# print(x)
t_list = []
for i in range(1000):
    t = threading.Thread(target=sub)
    t.start()
    t_list.append(t)

for t in t_list:
    t.join()

print(x)
