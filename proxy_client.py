import socket

BYTES_TO_READ = 4096

def get(host, port):
    request = b"GET / HTTP/1.1\nHost: www.google.com\n\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.send(request)
        s.shutdown(socket.SHUT_WR)
        chunck = s.recv(BYTES_TO_READ)
        result = b'' + chunck

        while(len(chunck) > 0):
            chunck = s.recv(BYTES_TO_READ)
            result += chunck
        s.close()
        return result
print(get("127.0.0.1", 8080))

