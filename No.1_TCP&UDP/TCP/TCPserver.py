#coding:utf-8

from socket import *
from time import ctime

print("=====================时间戳TCP服务器=====================");

HOST = ''  # 主机号为空白表示可以使用任何可用的地址。
PORT = 21567  # 端口号
BUFSIZ = 1024  # 接收数据缓冲大小
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM) # 创建TCP服务器套接字
tcpSerSock.bind(ADDR)  # 套接字与地址绑定
tcpSerSock.listen(5) # 监听连接，同时连接请求的最大数目

while True:
    print('等待客户端的连接...')
    tcpCliSock, addr = tcpSerSock.accept()   # 接收客户端连接请求
    print('取得连接:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)  # 连续接收指定字节的数据，接收到的是字节数组
        if not data:  # 如果数据空白，则表示客户端退出，所以退出接收
            break
        tcpCliSock.send(('[%s] %s' % (ctime(), data)).encode()) # 向客户端发送时间戳数据

    tcpCliSock.close()  # 关闭与客户端的连接

tcpSerSock.close()  # 关闭服务器socket