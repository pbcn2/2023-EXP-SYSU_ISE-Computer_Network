from socket import *
from time import ctime
import time

HOST = ''
PORT = 8080
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerrverSocket=socket(AF_INET,SOCK_DGRAM) # 创建UDP连接
udpSerrverSocket.bind(ADDR) # 绑定服务器地址

while True: # 服务器无限循环
    print('等待连接...')
    data,addr=udpSerrverSocket.recvfrom(BUFSIZ)  # 接受客户的连接
    # udpSerrverSocket.sendto(bytes('[%s] %s' % (ctime(),   data),encoding='utf-8'), addr) # 发送UDP 数据
    timestamp_ms = int(time.time() * 1000 + time.time_ns() % 1000000 // 1000)
    # 构造新的时间戳字符串
    timestamp_str = bytes('[%d] %s' % (timestamp_ms, data), encoding='utf-8')
    
    udpSerrverSocket.sendto(timestamp_str, addr) # 反馈给客户端同样的时间�
    print( '连接地址:', addr)
    
udpSerrverSocket.close() # 关闭服务器连接