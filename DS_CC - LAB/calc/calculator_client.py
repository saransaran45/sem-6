import socket

def start_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print("Connected to the calculator server")

    while True:
        expression = input("Enter an arithmetic expression (or 'exit' to quit): ")

        if expression.lower() == 'exit':
            break

        client_socket.sendall(expression.encode('utf-8'))

        result = client_socket.recv(1024).decode('utf-8')
        print(f"Result from server: {result}")

    print("Closing the connection to the server")
    client_socket.close()

if __name__ == "__main__":
    HOST = '127.0.0.1'  
    PORT = 12345        

    start_client(HOST, PORT)
