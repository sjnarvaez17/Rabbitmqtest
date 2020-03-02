"""
Basic AMQP consumer
only produces a "hello world" message
from Rabbitmq tutorials
Modified by JMA.
"""



import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))  # connect to server
channel = connection.channel()  # create a communication channel

channel.queue_declare(queue='hello')  # queue declaration


def callback(ch, method, properties, body):
	"""
	the callback method defines what to do when a message arrives
	"""
	print(" [x] Received %r" % body)


channel.basic_consume(  # how to consume the message
	queue='hello',  # which queue it will listen?
	on_message_callback=callback,  # Which method should be called on message arrival
	auto_ack=True)  # automatic aknowledgment activated.

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()  # initialize the consumer
