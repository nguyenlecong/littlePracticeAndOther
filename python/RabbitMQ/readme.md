# RabbitMQ

- **RabbitMQ** là một phần mềm cho phép xây dựng **Message Queue** theo protocol **AMQP** (Advanced Message Queue Protocol) và khá thông dụng trên thế giới. Để kết nối đến RabbitMQ trên Python, ta sẽ sử dụng thư viện **pika**
![rabbitmq1](https://images.viblo.asia/a1571d98-cb4e-4f3a-9757-117a492be32c.png)

- AMQP hay Advanced Message Queuing Protocol là tên gọi dùng để chỉ các giao thức xếp hàng tin nhắn nâng cao. Những giao thức này được ứng dụng cung cấp để để chuẩn mở cho các phần mềm trung gian hướng thông báo. Nhiệm vụ chính của AMQP là định hướng tin nhắn, xếp hàng, định tuyến, tăng độ tin cậy và bảo mật
- Message Broker là phần mềm dùng để giúp các ứng dụng khác nhau có thể giao tiếp với nhau một cách dễ dàng. Nó cũng được sử dụng như một ứng dụng trung chuyển tin nhắn và thông tin giữa các phần mềm khác nhau
- **RabbitMQ là gì?** RabbitMQ là một Message Broker sử dụng giao thức AMQP để phục vụ cho hoạt động trao đổi tin nhắn giữa các ứng dụng với nhau. RabbitMQ được hiểu như một người vận chuyển các message và quản lý những tin nhắn trên hàng đợi.
Nói chung, RabbitMQ được tạo ra với mục đích xử lý lượng lớn tin nhắn, thông điệp phức tạp giữa các ứng dụng với nhau. Nó giúp di chuyển, xử lý, biên dịch và lưu trữ các message
- RabbitMQ hoạt động như một bưu điện trung chuyển. Nhiệm vụ của nó là chờ người bán hàng mang hàng đến bưu cục và vận chuyển nó đến tay khách hàng. Khi một người có nhu cầu gửi thông tin, họ sẽ đẩy tin nhắn vào Message broker. Message broker sẽ tiếp nhận, lưu trữ bản sao và phiên dịch nếu cần thông tin đó. Rồi cuối cùng mới mang tin nhắn đến cho người dùng. Tại sao phải dùng RabbitMQ khi mà người gửi có thể trực tiếp send tin nhắn đến cho người nhận? Bạn chỉ có thể làm thủ công thế với những cuộc trao đổi 1:1. Khi một máy chủ cần phải gửi nhiều loại thông tin cho nhiều đối tượng khác nhau, RabbitMQ sẽ giúp tối ưu hóa quá trình này
- Một RabbitMQ sẽ bao gồm hai hoạt động chính đó là **exchange** và **queue**. Trong đó, exchange chịu trách nhiệm phân luồng thông tin thành các topic đã được cài trước khác nhau. Từ đó xác định đúng tin nhắn cho đúng đối tượng. Còn queue được hiểu như một danh sách chờ. Danh sách này bao gồm các tin nhắn được sắp xếp theo một thứ tự thời gian nhất định và lần lượt được gửi đi. Sau khi tin nhắn đã được gửi đi, nó tiếp tục phải chờ đợi nếu cho đến khi người nhận muốn lấy nó xuống. Tất nhiên là trong trường hợp người nhận cài đặt chế độ chờ thư như vậy trước
- **Có 5 loại Exchange:**
  - **Direct Exchange:**
    - đẩy message đến hàng chờ đợi dựa theo khóa định tuyến routing key
    - khá hữu ích khi bạn muốn phân biệt các thông báo được xuất bản cho cùng một trao đổi bằng cách sử dụng một mã định danh chuỗi đơn giản
    - Ví dụ, nếu hàng đợi gắn với một exchange có binding key là pdfprocess, message được đẩy vào exchange với routing key là pdfprocess sẽ được đưa vào hàng đợi.
  - **Fanout Exchange:**
    - đẩy message đến toàn bộ hàng đợi gắn với nó. Nó được xem là một bản copy message tới tất cả những hàng đợi với bất kể một routing key nào. Nếu được đăng ký thì nó sẽ bị bỏ qua
    - hữu ích với trường hợp ta cần một dữ liệu được gửi tới nhiều thiết bị khác nhau với cùng một message nhưng cách xử lý ở mỗi thiết bị, mỗi nơi là khác nhau
  - **Topic Exchange:**
    - sẽ làm một wildcard (lá bài) để gắn routing key với một routing pattern khai báo trong binding. Consumer có thể đăng ký những topic mà nó quan tâm. Cú pháp được sử dụng ở đây là * và #.
    -  Ví dụ: - booking.* -> Được đăng ký bởi tất cả những key với pattern bắt đầu bằng booking. - booking.# -> Được đăng ký bởi tất cả các key booking hoặc bắt đầu với booking
  - **Headers Exchange:**
    - Một header exchange sẽ dùng các thuộc tính header của message để định tuyến
    - Headers Exchange rất giống với Topic Exchange, nhưng nó định tuyến dựa trên các giá trị tiêu đề thay vì các khóa định tuyến. Một thông điệp được coi là phù hợp nếu giá trị của tiêu đề bằng với giá trị được chỉ định khi ràng buộc
  - **Dead Letter Exchange:**
    - Nếu không tìm thấy hàng đợi phù hợp cho tin nhắn, tin nhắn sẽ tự động bị hủy. RabbitMQ cung cấp một tiện ích mở rộng AMQP được gọi là “Dead Letter Exchange” — Cung cấp chức năng để chụp các tin nhắn không thể gửi được.
- **Các tính năng nổi bật của RabbitMQ:**
  - **Liên kết**
    - Đối với các server cần các kết nối không quá chặt chẽ và có độ tin cậy cao so với clustering cho phép, RabbitMQ cung cấp một mô hình liên kết phù hợp với yêu cầu này.
  - **Routing linh hoạt**
    - Tin nhắn sẽ được route thông qua trao đổi trước khi chuyển đến queue. RabbitMQ cung cấp một số loại trao đổi được tích hợp sẵn cho định tuyến logic điển hình. Với các định tuyến phức tạp hơn, bạn có thể liên kết các trao đổi với nhau hoặc thậm chí có thể viết các kiểu trao đổi của riêng bạn như một plugin.
  - **Clustering/cụm**
    - RabbitMQ có chức năng nhóm lại với nhau, hợp thành một nhà trung gian duy nhất.
  - **Độ tin cậy**
    - RabbitMQ hỗ trợ nhiều tính năng khác nhau cho phép bạn giao dịch các tác vụ một cách tin cậy, với thời gian lưu lâu hơn, xác nhận giao hàng, xác nhận của nhà xuất bản và tính khả dụng cao.
  - **Queue có tính sẵn sàng cao**
    - Queue có thể được nhân bản trên một số máy trong một cluster, đảm bảo cho tin nhắn của bạn luôn an toàn ngay cả khi xảy ra tình huống lỗi phần cứng.
  - **Đa giao thức**
    - RabbitMQ hỗ trợ messaging thông qua nhiều giao thức messaging khác nhau: AMQP, STOMP, MQTT, HTTP and Websocket
  - **Đa dạng ứng dụng ngôn ngữ**
    - RabbitMQ hiện đã được phát triển với hệ ngôn ngữ phong phú bao gồm hầu hết mọi ngôn ngữ bạn có thể nghĩ đến.
  - **Giao diện quản lý**
    - Với giao diện quản lý sử dụng dễ dàng, RabbitMQ cho phép bạn theo dõi và kiểm soát mọi vấn đề trong chương trình messaging trung gian.
  - **Hệ thống plugin**
    - RabbitMQ hỗ trợ một loạt các phần mở rộng của plugin dưới nhiều hình thức khác nhau hoặc bạn cũng có thể tự viết các tiện ích mở rộng này.
  - **Tracing/Truy vết**
    - Nếu hệ thống messaging của bạn bị lỗi hoặc hoạt động không tốt, RabbitMQ sẽ hỗ trợ các thao tác truy vết để giúp bạn hiểu được hệ thống đang hoạt động như thế nào và vấn đề nào đang phát sinh.
- [RabbitMQ performance với Python P1](https://www.phamquangloc.vn/2020/08/reference-test-RabbitMQ-performance-voi-python-dung-pika.html)
- [RabbitMQ performance với Python P2](https://www.phamquangloc.vn/2020/08/reference-chem-gio-hiep-2-ve-send-file-dung-luong-lon-qua-RabbitMQ-voi-python-pika.html)
