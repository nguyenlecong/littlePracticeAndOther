import pika

'''
Để gởi một message, chúng ta cần kết nối đến server và khai báo một channel,
ở đây là channel có tên là hello
'''
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print("Sent 'Hello World!'")

connection.close()
