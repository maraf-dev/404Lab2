import socket
from threading import Thread

BYTES_TO_READ = 4096
Host = "127.0.0.1"
Port = 8080

def handle_connection(conn, addr):
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(BYTES_TO_READ) # wait for request, and read it
            if not data:
                break
            print(data)
            conn.sendall(data) # send it back to the client

# start single threaded echo server
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((Host, Port))
        s.listen()
        while True:
            conn, addr = s.accept()
            handle_connection(conn, addr)

# start multi threaded echo server
def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((Host, Port))
        s.listen(2)
        while True:
            conn, addr = s.accept()
            thread = Thread(target=handle_connection, args=(conn, addr))
            thread.run()

# start_server()
start_threaded_server()