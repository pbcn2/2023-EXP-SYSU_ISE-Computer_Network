import socket

HOST = '127.0.0.1'  # 监听地址为本地回环地址
PORT = 8080  # 监听端口为 8080
DOC_ROOT = './helloworld.html'  # 静态文件所在目录为当前目录下的 www 子目录

# 定义 HTTP 响应头，status_code 表示 HTTP 状态码
def get_response_header(status_code):
    if status_code == 200:  # 如果状态码为 200，表示成功响应，返回 200 OK
        return 'HTTP/1.1 200 OK\r\n\r\n'
    elif status_code == 404:  # 如果状态码为 404，表示请求的文件不存在，返回 404 Not Found
        return 'HTTP/1.1 404 Not Found\r\n\r\n'
    else:  # 否则返回 500 Internal Server Error
        return 'HTTP/1.1 500 Internal Server Error\r\n\r\n'

# 处理 HTTP 请求
def handle_request(conn):
    # 接收客户端发来的请求数据
    request = conn.recv(1024).decode()
    # 从套接字对象 conn 中最多读取 1024 个字节的数据。
    # 然后，decode() 方法将读取的字节数据解码成字符串，并将其赋值给变量 request
    if not request:  # 如果请求为空，返回 500
        conn.sendall(get_response_header(500).encode())
        # 向客户端发送 HTTP 状态码为 500 的响应头字符串，并告诉客户端服务器无法处理客户端的请求。
        return

    # 解析请求，获取请求的文件名
    filename = request.split(' ')[1].lstrip('/')
    if filename == '':  # 如果请求的文件名为空，表示访问根目录，返回 index.html
        filename = 'index.html'
    filepath = DOC_ROOT + '/' + filename

    # 打开文件并读取文件内容
    try:
        with open(filepath, 'rb') as f:
            content = f.read()
            # 将文件内容和响应头返回给客户端
            conn.sendall(get_response_header(200).encode() + content)
    except IOError:  # 如果文件不存在，返回 404
        conn.sendall(get_response_header(404).encode())

# 创建 socket，绑定地址和端口并监听连接
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # 使用 with...as... 语句可以在代码块结束时自动关闭套接字对象，避免套接字资源的泄露或占用。
    s.bind((HOST, PORT))
    s.listen()

    # 循环接受客户端的连接并处理请求
    while True:
        # 接受客户端连接，阻塞模式
        conn, addr = s.accept()
        # 套接字对象 conn 和客户端的地址信息 addr
        with conn:
            # 处理客户端请求
            handle_request(conn)
