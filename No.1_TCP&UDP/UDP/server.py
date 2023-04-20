from socket import *
from time import ctime

HOST = ''
PORT = 8080
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerrverSocket=socket(AF_INET,SOCK_DGRAM) # 创建UDP连接
udpSerrverSocket.bind(ADDR) # 绑定服务器地址

while True: # 服务器无线循环
    print('等待连接...')
    data,addr=udpSerrverSocket.recvfrom(BUFSIZ)  # 接受客户的连接
    udpSerrverSocket.sendto(bytes('[%s] %s' % (ctime(),   data),encoding='utf-8'), addr) # 发送UDP 数据
    print( '连接地址:', addr)
    
udpSerrverSocket.close() # 关闭服务器连接