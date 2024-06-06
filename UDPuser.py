# udp_client.py

import socket


def start_udp_client(host='127.0.0.1', port=12346):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        server_address = (host, port)

        while True:
            message = input("请输入消息：")
            if message.lower() == 'exit':
                break
            client_socket.sendto(message.encode('utf-8'), server_address)
            data, _ = client_socket.recvfrom(1024)
            response = data.decode('utf-8')
            print(f"服务器响应: {response}")


if __name__ == "__main__":
    start_udp_client()
