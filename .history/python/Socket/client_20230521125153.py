import socket

# Tạo socket
s = socket.socket()

# Tạo kết nối với server
host = '127.0.0.1'
port = 12345
s.connect((host, port))

#  Đọc sữ liệu được server gửi tới recv()
print(s.recv(1024))

# Đóng socket
s.close
