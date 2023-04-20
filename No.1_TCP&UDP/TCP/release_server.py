# from socket import *
# # 准备服务器端socket
# serverSocket = socket(AF_INET, SOCK_STREAM)
# while True:
#     print("Ready to serve...")
#     connectionSocket, addr = serverSocket.accept()
#     try:
#         message = 
#         filename = message.split()[1]
#         f = open(filename[1:])
#         # 通过 socket 发送 HTTP 头部
#         outputdata = 
#         for i in range(0, len(outputdata)):
#             connectionSocket.send(outputdata[i])
#         connectionSocket.close()
#     except IOError:
#         # 发送未找到文件的响应消息（按需补充代码）
#         # 关闭客户端 socket （按需补充代码）

# serverSocket.close()


from socket import *

# 定义服务器地址和端口
serverHost = ''
serverPort = 8080

# 准备服务器端 socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverHost, serverPort))
serverSocket.listen(1)

while True:
    print("Ready to serve...")

    # 接受客户端连接请求
    connectionSocket, addr = serverSocket.accept()

    try:
        # 接收客户端发送的 HTTP 请求消息
        message = connectionSocket.recv(1024).decode()
        if not message:
            continue

        # 获取客户端请求的文件名
        filename = message.split()[1].lstrip('/')

        # 打开文件并读取文件内容
        with open(filename, 'rb') as f:
            content = f.read()
            # 构造 HTTP 响应消息头部
            response = 'HTTP/1.1 200 OK\r\n' + \
                       'Content-Type: text/html; charset=UTF-8\r\n' + \
                       'Content-Length: {}\r\n'.format(len(content)) + \
                       '\r\n'

            # 将响应消息头部和文件内容发送给客户端
            connectionSocket.send(response.encode())
            connectionSocket.send(content)
    except IOError:
        # 如果文件不存在，发送 404 Not Found 响应消息
        response = 'HTTP/1.1 404 Not Found\r\n\r\n'
        connectionSocket.send(response.encode())
    finally:
        # 关闭客户端 socket
        connectionSocket.close()

# 关闭服务器 socket
serverSocket.close()
