import pika

'''
gởi message khai báo một worker xử lý các message nhận được từ channel hello .có nội dung Hello World! thông qua channel này, kèm theo khai báo routing_key là hello . Routing Key sẽ giúp điều hướng message này đến đúng các worker được khai báo nhận message theo routing key (Consumer)
'''
connection = pika.BlockingConnection(pika.Connectio
nParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
print ' [*] Waiting for messages. To exit press CTR
L+C'
def callback(ch, method, properties, body):
print " [x] Received %r" % (body,)
channel.basic_consume(callback, queue='hello'
, no_a
ck=True)
channel.start_consuming()
