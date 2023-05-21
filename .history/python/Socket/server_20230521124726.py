import socket

# Tạo ra một máy chủ bằng cách mở một socket - Socket()
s = socket.socket()

# Liên kết nó với một host hoặc một máy và một port - Bind()
host = socket.gethostname()
port = 12345
s.bind((host, port))

# rt đó - Listen()oặc một máy và một port - Bind()
s.listen(5)
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send('Thank you for connecting')
    c.close()
