import socket

def start_server(port):
    """
    Starts a simple web server that listens on the given port.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(1)
    print(f"Server is listening on port {port}")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address}")

        try:
            response_headers = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n"
            client_socket.send(response_headers.encode())

            response_body = "Hello, connection received!"
            client_socket.send(response_body.encode())

            client_socket.shutdown(socket.SHUT_WR)
            client_socket.recv(1024) 
        except ConnectionResetError:
            print("Client closed the connection abruptly.")
        finally:
            client_socket.close()

if __name__ == '__main__':
    port = 8000
    start_server(port)