import pika

'''
khai báo một worker xử lý các message nhận được từ
channel hello
'''
connection = pika.BlockingConnection(
    pika.ConnectionParameters('127.0.0.1'))
channel = connection.channel()

channel.queue_declare(queue='hello')

print('[*] Waiting for messages. To exit press CTRL+C')

'''
vì là consumer nên sẽ sử dụng phương thức basic_consume
để lắng nghe trên queue hello , khi có message đến sẽ gọi
hàm callback() để xử lý
'''


def callback(ch, method, properties, body):
    print("[x] Received %r" % (body,))


channel.basic_consume(callback, queue='hello', no_ack=True)

channel.start_consuming()
