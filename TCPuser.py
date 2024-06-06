# tcp_client.py

import socket

def start_tcp_client(host='127.0.0.1', port=12346):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"已连接到服务器{host}:{port}")

        while True:
            message = input("请输入消息：")
            if message.lower() == 'exit':
                break
            client_socket.sendall(message.encode('utf-8'))
            data = client_socket.recv(1024)
            response = data.decode('utf-8')
            print(f"服务器响应: {response}")

if __name__ == "__main__":
    start_tcp_client()


