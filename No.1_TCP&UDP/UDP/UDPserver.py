from socket import *
port=12000
socket_server=socket(AF_INET,SOCK_DGRAM)
socket_server.bind(('',port))
message_server="I'm server!"
while True:
    message,address_client=socket_server.recvfrom(1024)
    print('The address of client is:',address_client)
    print('The message from client is:',message.decode())
    socket_server.sendto(message_server.encode(),address_client)
