import socket
s = socket.socket()
host = '130.215.14.89'
port = 8080
s.connect((host, port))
print(s.recv(1024))
s.close()
