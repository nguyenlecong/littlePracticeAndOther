import socket

# Tạo socket
s = socket.socket()

# Tạo kết nối với server
host = '127.0.0.1'
port = 12345
s.connect((host, port))

#  Đọc sữ liệu được server gửi tới recv()
# 1024 là số bytes mà client có thể nhận được trong 1 lần
msg = 
print()

# Đóng socket
s.close()
