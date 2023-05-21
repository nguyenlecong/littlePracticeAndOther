import pika

'''
khai báo một worker xử lý các message nhận được từ channel hello .
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
