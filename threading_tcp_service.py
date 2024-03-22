import socket
import threading


def handle_client_request(service_client_socket, ip_port):
    while True:
        recv_data = service_client_socket.recv(1024)
        if recv_data:
            recv_content = recv_data.decode('utf-8')
            print(f'Received {recv_content},form {ip_port}')
            service_client_socket.send('Successfully received'.encode('utf-8'))
        else:
            print('Connection closed')
            break
    service_client_socket.close()


if __name__ == '__main__':
    service_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    service_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    service_socket.bind(('', 8989))
    service_socket.listen(128)
    while True:
        service_client_socket, ip_port = service_socket.accept()
        print('Connection created successfully')
        thread = threading.Thread(target=handle_client_request, args=(service_client_socket, ip_port))
        thread.setDaemon(True)
        thread.start()
    # service_socket.close()
