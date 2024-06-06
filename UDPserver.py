# udp_server.py

import socket

def start_udp_server(host='127.0.0.1', port=12346):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        print(f"UDP服务器已启动，正在监听{host}:{port}...")

        while True:
            data, client_address = server_socket.recvfrom(1024)
            message = data.decode('utf-8')
            print(f"收到来自{client_address}的消息: {message}")
            server_socket.sendto('消息已收到'.encode('utf-8'), client_address)

if __name__ == "__main__":
    start_udp_server()
