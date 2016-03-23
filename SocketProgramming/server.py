import socket

s = socket.socket()
host = '130.215.14.89'
port = 8080
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print('Got connection from',addr)
    c.send('Thank you for connecting')
    c.close()
