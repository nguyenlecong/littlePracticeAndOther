import time

import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
channel = connection.channel()
channel.queue_declare(queue='test-queues')

for i in range(999):
    data = 'Message No. : {}'.format(i)
    channel.basic_publish(exchange='test-exchanges', routing_key='test-queues', body=data)
    print("[x] Meesage sent to consumer", i)
    time.sleep(0.1)

connection.close()