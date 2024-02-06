import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Accepted connection from {client_address}")

    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break

            print(f"Received from {client_address}: {data}")

            result = calculate(data)

            client_socket.sendall(str(result).encode('utf-8'))
        except Exception as e:
            print(f"Error: {e}")
            break

    print(f"Connection from {client_address} closed.")
    client_socket.close()

def calculate(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        print(f"Calculation error: {e}")
        return "Error"

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    HOST = '127.0.0.1'  
    PORT = 12345        

    start_server(HOST, PORT)
