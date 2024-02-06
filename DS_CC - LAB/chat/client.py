import socket
import threading

def send(client):
    while True:
        mes = input("Enter a mes to be send:")
        client.send(mes.encode('utf-8'))

def recv(client):
    while True:
        mes = client.recv(1024).decode('utf-8')
        print(f"{mes}")

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1',55555))

    t1 = threading.Thread(target=send,args=(client,))
    t2 = threading.Thread(target=recv,args=(client,))

    t1.start();
    t2.start();

    t1.join()
    t2.join()


main()
