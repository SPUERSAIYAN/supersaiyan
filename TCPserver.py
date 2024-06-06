# tcp_server.py

import socket

def start_tcp_server(host='127.0.0.1', port=12346):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"TCP服务器已启动，正在监听{host}:{port}...")

        while True:
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"与客户端{client_address}建立连接")
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    message = data.decode('utf-8')
                    print(f"收到消息: {message}")
                    client_socket.sendall('消息已收到'.encode('utf-8'))

if __name__ == "__main__":
    start_tcp_server()

