from socket import *
from datetime import datetime
import threading 

HOST = '172.28.7.231'  # 服务器连接地址
PORT = 8080  # 服务器启用端口
BUFSIZ = 1024  # 缓冲区大小
ADDR = (HOST, PORT)

udpCliendSocket = socket(AF_INET, SOCK_DGRAM)

# 一个计数变量
count = 0
time_start = ''
time_end = 0
ADDA = 0

def recv_timeout():
    try:
        data, ADDR = udpCliendSocket.recvfrom(BUFSIZ)
    except timeout:
        print("recv timeout")
        return
    if not data:
        return
    if len(data) != 14:  # 如果不是时间戳数据包，直接跳过本次循环
        return
    global time_start, time_end, count
    if not time_start:
        time_start = data
    time_end = data
    count += 1

for i in range(10):
    i = str(i)
    data = bytes(i, encoding="UTF-8")
    ADDR = (HOST, PORT)  # 在每次循环中更新ADDR的值
    udpCliendSocket.sendto(data, ADDR)

    udpCliendSocket.settimeout(1)  # 设置超时时间为1秒
    timer = threading.Timer(1.1, recv_timeout)  # 创建定时器线程，超时时间为1秒
    timer.start()  # 启动定时器线程
    data, ADDR = None, None
    try:
        data, ADDR = udpCliendSocket.recvfrom(BUFSIZ)
        if not time_start:
            time_start = data
        time_end = data
        count += 1
        continue
    except timeout:
        print("recv timeout")
        timer.cancel()  # 取消定时器线程
        continue  # 超时后使用continue跳过本轮循环
    finally:
        udpCliendSocket.settimeout(None)  # 恢复默认的超时时间
        timer.cancel()  # 取消定时器线程


# 将时间戳bytes字符串转换为字符串，并使用切片操作获取时间戳部分
if time_start:
    time_start = int(time_start.hex(), 16)  # 将 bytes 对象转换为整数
    time_end = int(time_end.hex(), 16)
    time_start = str(time_start)[1:14]  # 将整数转换为字符串，并使用切片操作获取时间戳部分
    time_end = str(time_end)[1:14]

# 将时间戳字符串转换为datetime对象，计算时间差，并输出结果
if time_start:
    dt1 = datetime.fromtimestamp(int(time_start) / 1000)
    dt2 = datetime.fromtimestamp(int(time_end) / 1000)
    print(dt1, dt2)
    delta = dt2 - dt1

    # 总共发送了十个数据包，count用于计数已经收到了的个数，输出丢失率
    print(ADDR, "的统计信息：")
    print("\t 数据包：已发送 = 10, 已接收 =", count, ", 丢失 =", 10 - count, "(", 100 * (10 - count) / 10, "% 丢失)")
    print("往返行程的总时间：")
    print("\t",delta)
    
udpCliendSocket.close()
