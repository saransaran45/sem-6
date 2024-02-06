import socket
import threading

def recv(client_socket):
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        print(f"Client :{data}")

def send(client_socket):
    while True:
        mes = input()
        client_socket.send(f"server :{mes}".encode('utf-8'))


def main():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('127.0.0.1',55555))
    server.listen(5)
    print("server listening on 5555")

    client,addr = server.accept()
    print(f"Accepted connection from {addr}")
    th1 = threading.Thread(target=send,args=(client,))
    th2 = threading.Thread(target=recv,args=(client,))
        
    th1.start()
    th2.start()

    th1.join()
    th2.join()
if __name__ == "__main__":
    main()