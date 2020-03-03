"""
Basic AMQP consumer
only produces a "hello world" message
from Rabbitmq tutorials
Modified by JMA.
"""



import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
	"""
	the callback method defines what to do when a message arrives
	"""
	print(" [x] Received %r" % body)


channel.basic_consume(  # how to consume the message
	queue=queue_name,  # which queue it will listen?
	on_message_callback=callback,  # Which method should be called on message arrival
	auto_ack=True)  # automatic acknowledgment activated.

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()  # initialize the consumer
