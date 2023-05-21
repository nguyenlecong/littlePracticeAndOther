import pika

'''
Để gởi một message, chúng ta cần kết nối đến server
và khai báo một channel, ở đây là channel có tên là hello
'''
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

'''
Gửi message có nội dung Hello World! thông qua channel này,
kèm theo khai báo routing_key là hello.
Routing Key sẽ giúp điều hướng message này đến đúng các worker
được khai báo nhận message theo routing key (Consumer)
'''
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print("[x] Sent 'Hello World!'")

connection.close()
