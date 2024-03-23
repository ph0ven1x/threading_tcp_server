import socket
import threading


def handle_client_request(server_client_socket, ip_port):
    while True:
        recv_data = server_client_socket.recv(1024)
        if recv_data:
            recv_content = recv_data.decode('utf-8')
            print('Received {},form {}'.format(recv_content, ip_port))
            server_client_socket.send('Successfully received'.encode('utf-8'))
        else:
            print('Connection to {} was closed'.format(ip_port))
            break
    server_client_socket.close()


if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server_socket.bind(('', 8989))
    server_socket.listen(128)
    while True:
        server_client_socket, ip_port = server_socket.accept()
        print('Connection created successfully')
        thread = threading.Thread(target=handle_client_request, args=(server_client_socket, ip_port))
        thread.setDaemon(True)
        thread.start()
    # server_socket.close()
