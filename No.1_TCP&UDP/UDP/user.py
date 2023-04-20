from socket import *

HOST = '192.168.2.24'  # 服务器连接地址
PORT = 8080  # 服务器启用端口
BUFSIZ = 1024  # 缓冲区大小
ADDR = (HOST, PORT)

udpCliendSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    data = bytes(input('> '), encoding="UTF-8")
    if not data:
        break   
    udpCliendSocket.sendto(data, ADDR)
    data, ADDR = udpCliendSocket.recvfrom(BUFSIZ)
    if not data:
        break   
    print (data)
    
udpCliendSocket.close()