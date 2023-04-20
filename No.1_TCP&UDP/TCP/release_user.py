
import socket

# 定义服务器地址和端口
serverHost = '172.28.20.78'
serverPort = 8080

# 创建客户端 socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接到服务器
clientSocket.connect((serverHost, serverPort))

# 发送 HTTP GET 请求
request = 'GET /helloworld.html HTTP/1.1\r\nHost: {}\r\n\r\n'.format(serverHost)
clientSocket.send(request.encode())

# 接收服务器响应
response = clientSocket.recv(1024).decode()

# 输出服务器响应的内容
print(response)

# 关闭客户端 socket
clientSocket.close()
