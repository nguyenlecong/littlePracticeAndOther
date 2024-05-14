# Socket[^1]
- **Python networking**
  - Python có 2 level để truy cập đến các dịch vụ mạng:
    - Ở low-level, có thể truy cập đến Socket của Hệ điều hành, nơi cho phép tác động Client - Server bằng cả 2 giao thức Connection-oriented (kết nối định tuyến) và Connectionless (kết nối bất định tuyến)
    - Ngoài ra, Python còn cung cấp 1 số thư viện để truy cập đến các giao thức High-level như HTTP, FTP…
- **Socket là gì**
  - Socket là giao diện lập trình ứng dụng mạng được dùng để **truyền và nhận dữ liệu trên internet**. Giữa hai chương trình chạy trên mạng cần có một liên kết giao tiếp hai chiều (two-way communication) để kết nối 2 process trò chuyện với nhau. Một socket là một end-point của một liên kết giữa hai ứng dụng
  - Một chức năng khác của socket là **giúp các tầng TCP hoặc TCP Layer định danh ứng dụng mà dữ liệu sẽ được gửi tới** thông qua sự ràng buộc với một cổng port (thể hiện là một con số cụ thể), từ đó tiến hành kết nối giữa client và server
  - Có 2 loại socket thường thấy đó là dùng giao thức TCP hoặc UDP
- **Stream Sockets**
  - Dựa trên giao thức TCP (Tranmission Control Protocol) việc truyền dữ liệu chỉ thực hiện giữa 2 quá trình đã thiết lập kết nối. Giao thức này đảm bảo dữ liệu được truyền đến nơi nhận một cách **đáng tin cậy**, **đúng thứ tự** nhờ vào cơ chế quản lý luồng lưu thông trên mạng và cơ chế chống tắc nghẽn
- **Datagram Socket**
  - Dựa trên giao thức UDP (User Datagram Protocol) việc truyền dữ liệu không yêu cầu có sự thiết lập kết nối giữa 2 quá trình
  - Ngược lại với giao thức TCP thì dữ liệu được truyền theo giao thức UDP **không được tin cậy**, **có thế không đúng trình tự và lặp lại**. Tuy nhiên vì nó không yêu cầu thiết lập kết nối không phải có những cơ chế phức tạp nên **tốc độ nhanh**…ứng dụng cho các ứng dụng truyền dữ liệu nhanh như chat, game…
- **Port**
  - Port **xác định duy nhất một tiến trình** (process) trên một máy trong mạng. Hay nói cách khác là cách mà phân biệt giữa các ứng dụng chạy trên máy tính
  - Một TCP/IP Socket gồm một địa chỉ IP kết hợp với một port xác định duy nhất một tiến trình (process) trên mạng. Hay nói cách khác luồng thông tin trên mạng dựa vào **IP là để xác định một máy còn port xác định 1 tiến trình** trên 1 máy
- **Client – Server**
  - **Server** có nhiệm vụ của là **lắng nghe, chờ đợi kết nối từ Client** trên địa chỉ IP của mình với PORT được quy định sẵn. Khi **client gửi dữ liệu** tới Server thì nó phải giải quyết một công việc là **nhận dữ liệu đó -> xử lý -> trả kết quả** lại cho Client
  - **Client** là ứng dụng được phục vụ, nó **chỉ gửi truy vấn và chờ đợi kết quả** từ Server
- **Python Socket**
  - Để tạo 1 socket ta làm như sau: `s = socket.socket (socket_family, socket_type)`

|Term|Description|
|----|-----------|
|domain|Họ của các giao thức dùng để truyền dữ liệu: AF_INET, PF_INET, PF_UNIX, PF_X25… Ở đây chúng ta thường dùng AF_INET (IPv4)|
|type|Kiểu của socket: SOCK_STREAM (TCP), SOCK_DGRAM (UDP)|
|protocol|Dùng để xác định các biến thể của các giao thức, mặc định là 0|
|hostname|Dùng để xác định hostname, có thể là: Chuỗi, Địa chỉ IPv4 nếu dùng AF_INET, Địa chỉ IPv6 nếu dùng AF_INET6|
|port|Xác định port của socket|

- **Server Socket Methods**

|Method|Description|
|------|-----------|
|s.bind()|Kết nối (hostname, port number) đến socket|
|s.listen()|Cho Server lắng nghe các Client|
|s.accept()|Thiết lập kết nối giữa Client-Server|

- **Client Socket Methods**
|Method|Description|
|------|-----------|
|s.connect()|Kết nối đến Server|

- **General Socket Methods**

|Method|Description|
|------|-----------|
|s.recv()|Nhận dữ liệu trong giao thức TCP|
|s.send()|Truyền dữ liệu trong giao thức TCP|
|s.recvfrom()|Nhận dữ liệu trong giao thức UDP|
|s.sendto()|Truyền dữ liệu trong giao thức UDP|
|s.close()|Đóng kết nối|
|socket.gethostname()|Trả về tên của host|

[^1]: [Python Sockets](https://pailema.edu.vn/cdn/uploadv2/news/1582267553_basic_lesson-13-python-socket.pdf)