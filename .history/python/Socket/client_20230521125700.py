import socket

# Tạo socket
s = socket.socket()

# Tạo kết nối với server
s.connect(("localhost", 4000))
s.connect((host, port))

#  Đọc sữ liệu được server gửi tới recv()
# 1024 là số bytes mà client có thể nhận được trong 1 lần
while True:
    msg = s.recv(1024)
    print(msg)

    # Đóng socket
    s.close()
