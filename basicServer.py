'''
Basic AMQP prooducer
only produces a "hello world" message
from Rabbitmq tutorials
Modified by JMA.
'''

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))  # connect to server
channel = connection.channel()  # create a communication channel
channel.queue_declare(queue='hello')  # queue declaration
for i in range (10):
    channel.basic_publish(exchange='',  # publish a message on a blank exchange
                      routing_key='hello',  # on the hello queue
                      body='Hello World!!!'+str(i))  # and the message's body is 'hello world'
    print(" [x] Sent 'Hello World!'")
    # time.sleep(1)
connection.close()
