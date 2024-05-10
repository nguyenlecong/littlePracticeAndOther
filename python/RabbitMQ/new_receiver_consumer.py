import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
channel = connection.channel()

channel.queue_declare(queue='test-queues')

print('[*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print("[x] Received %r" % (body,))

channel.basic_consume(on_message_callback=callback, queue='test-queues', auto_ack=True)

channel.start_consuming()
connection.close()