import socket

# Tạo ra một máy chủ bằng cách mở một socket - Socket()
s = socket.socket()

# Liên kết nó với một host hoặc một máy và một port - Bind()
host = 'localhost'
port = 4000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

# server sẽ bắt đầu lắng nghe trên port đó - Listen()
s.listen(1)  # số lượng tối đa các kết nối đang chờ

while True:
    # Chờ/chấp nhận kết nối accept ()
    # Hàm này trả về hai giá tri
    # c: kết nối; addr: địa chỉ của request hoặc địa chỉ của client
    c, addr = s.accept()
    print('Got connection from', addr)

    # gửi dữ liệu
    msg = input('Tin nhan: ').encode('utf-8')
    c.send(msg)

    # đóng kết nối
    c.close()
