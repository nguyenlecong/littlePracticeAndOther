import pika
connection = pika.BlockingConnection(pika.Connectio
nParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange=''
, routing_key='hel
lo'
, body='Hello World!')
print " [x] Sent 'Hello World!'"
connection.close()
