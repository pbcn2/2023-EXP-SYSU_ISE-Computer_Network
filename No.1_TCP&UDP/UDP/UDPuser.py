from socket import *
server='192.168.2.24'
server_port=12000
socket_client=socket(AF_INET,SOCK_DGRAM) # AF_INET表示使用IPv4，SOCK_DGRAM表示使用UDP套接字

for i in range(10):
    message="this is NO."
    socket_client.sendto(message.encode(),(server,server_port)) # 两台主机之间建立通信是通过进程的进行的，因此需要明确端口号(当然首先要明确主机地址)
    message_receive,address_server=socket_client.recvfrom(1024) # 1024表示缓存长度


print("The address of server is:",address_server)
print("The message from server is:",message_receive.decode())


socket_client.close()
