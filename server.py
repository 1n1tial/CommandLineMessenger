import socket
import threading

def handle_client(client_socket, address):
    print(f"Accepted connection from {address}")

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print(f"Connection with {address} closed.")
                break

            print(f"Received message from {address}: {message}")

            client_socket.send(message.encode('utf-8'))
        except ConnectionResetError:
            print(f"Connection with {address} reset by peer.")
            break
        
    client_socket.close()

def main():
    host = '127.0.0.1'
    port = 5555

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, address))
        client_handler.start()

if __name__ == "__main__":
    main()
