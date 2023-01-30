import pika
from SchlafenPubSub.base import base_pub_sub
from SchlafenPubSub.setting import schlafen_pubsub_ip, schlafen_pubsub_port, schlafen_pubsub_user, \
    schlafen_pubsub_password

"""
基于base 创建各个种类exchange
connection(TCP) -->  channel -->  queue + exchange 
"""


class publisher(base_pub_sub):
    """
    广播式的发布者 channel内queue的消息 通过交换机 被所有订阅者接收 不用考虑路由key
    """

    def __init__(self, host=schlafen_pubsub_ip, port=schlafen_pubsub_port, user=schlafen_pubsub_user,
                 password=schlafen_pubsub_password, channel_number=1, queue_name='', routing_key='default', exchange='',
                 exchange_type='fanout', vhost='/', durable=False):
        super().__init__(host, port, user, password, channel_number,
                         queue_name, routing_key, exchange, exchange_type, vhost)
        # queue：队列名 durable：是否持久化
        self.channel.queue_declare(
            self.queue_name, auto_delete=True, exclusive=True)
        # 指定交换机和类型
        self.channel.exchange_declare(exchange=exchange,
                                      exchange_type='fanout',
                                      passive=False,
                                      durable=durable,
                                      auto_delete=False)
        self.channel.confirm_delivery()  # #RabbitMQ收到消息后，将返回basic.ack(收到消息)或basic.nack(未收到消息)。
        self.routing_key = routing_key

    def pub(self, text):
        # channel.basic_publish向队列中发送信息
        # exchange -- 它使我们能够确切地指定消息应该到哪个队列去。
        # routing_key 指定向哪个队列中发送消息
        # body是要插入的内容, 字符串格式
        if isinstance(text, bytes):
            content_type = 'text/plain'
        elif isinstance(text, str):
            content_type = 'text/plain'
        elif isinstance(text, dict):
            content_type = 'application/json'
        try:
            if self.channel.basic_publish(exchange=self.exchange,
                                          routing_key=self.routing_key,
                                          body=text,
                                          properties=pika.BasicProperties(content_type=content_type,
                                                                          delivery_mode=1)):
                # print('Message publish was confirmed')
                pass
            else:

                print('Message could not be confirmed. TRY REPUB')
                self.repub(text)
        except Exception as e:
            print(e)
            self.reconnect().channel.basic_publish(exchange=self.exchange,
                                                   routing_key=self.routing_key,
                                                   body=text,
                                                   properties=pika.BasicProperties(content_type=content_type,
                                                                                   delivery_mode=1))

    def exit(self):
        self.connection.close()

    def repub(self, text):
        self.pub(text)


class publisher_routing(base_pub_sub):
    def __init__(self, host=schlafen_pubsub_ip, port=schlafen_pubsub_port, user=schlafen_pubsub_user,
                 password=schlafen_pubsub_password, channel_number=1, queue_name='', routing_key='default', exchange='',
                 exchange_type='direct', vhost='/', durable=False):
        super().__init__(host, port, user, password, channel_number,
                         queue_name, routing_key, exchange, exchange_type, vhost)
        self.routing_key = routing_key
        self.channel.queue_declare(
            self.queue_name, auto_delete=True, exclusive=True)
        self.channel.confirm_delivery()
        self.channel.exchange_declare(exchange=exchange,
                                      exchange_type=exchange_type,
                                      passive=False,
                                      durable=durable,
                                      auto_delete=False)

    def pub(self, text, routing_key):
        # channel.basic_publish向队列中发送信息
        # exchange -- 它使我们能够确切地指定消息应该到哪个队列去。
        # routing_key 指定向哪个队列中发送消息
        # body是要插入的内容, 字符串格式
        if isinstance(text, bytes):
            content_type = 'text/plain'
        elif isinstance(text, str):
            content_type = 'text/plain'
        elif isinstance(text, dict):
            content_type = 'application/json'
        try:
            if self.channel.basic_publish(exchange=self.exchange,
                                          routing_key=routing_key,
                                          body=text,
                                          properties=pika.BasicProperties(content_type=content_type,
                                                                          delivery_mode=1)):
                # print('Message publish was confirmed')
                pass
            else:
                print('Message could not be confirmed. TRY REPUB')
                self.repub(text, routing_key)
        except Exception as e:
            print(e)
            self.reconnect().channel.basic_publish(exchange=self.exchange,
                                                   routing_key=routing_key,
                                                   body=text,
                                                   properties=pika.BasicProperties(content_type=content_type,
                                                                                   delivery_mode=1))

    def exit(self):
        self.connection.close()

    def repub(self, text, routing_key):
        print('repub')
        self.pub(text, routing_key)


class publisher_topic(base_pub_sub):
    def __init__(self, host=schlafen_pubsub_ip, port=schlafen_pubsub_port, user=schlafen_pubsub_user,
                 password=schlafen_pubsub_password, channel_number=1, queue_name='', routing_key='default', exchange='',
                 exchange_type='topic', vhost='/', durable=False):
        super().__init__(host, port, user, password, channel_number,
                         queue_name, routing_key, exchange, exchange_type, vhost)
        self.routing_key = routing_key
        self.channel.queue_declare(
            self.queue_name, auto_delete=True, exclusive=True)
        self.channel.confirm_delivery()
        self.channel.exchange_declare(exchange=exchange,
                                      exchange_type=exchange_type,
                                      passive=False,
                                      durable=durable,
                                      auto_delete=False)

    def pub(self, text, routing_key):
        # channel.basic_publish向队列中发送信息
        # exchange -- 它使我们能够确切地指定消息应该到哪个队列去。
        # routing_key 指定向哪个队列中发送消息
        # body是要插入的内容, 字符串格式
        if isinstance(text, bytes):
            content_type = 'text/plain'
        elif isinstance(text, str):
            content_type = 'text/plain'
        elif isinstance(text, dict):
            content_type = 'application/json'
        try:
            if self.channel.basic_publish(exchange=self.exchange,
                                          routing_key=routing_key,
                                          body=text,
                                          properties=pika.BasicProperties(content_type=content_type,
                                                                          delivery_mode=1)):
                # print('Message publish was confirmed')
                pass
            else:
                print('Message could not be confirmed. TRY REPUB')
                self.repub(text, routing_key)
        except Exception as e:
            print(e)
            self.reconnect().channel.basic_publish(exchange=self.exchange,
                                                   routing_key=routing_key,
                                                   body=text,
                                                   properties=pika.BasicProperties(content_type=content_type,
                                                                                   delivery_mode=1))

    def exit(self):
        self.connection.close()

    def repub(self, text, routing_key):
        print('repub')
        self.pub(text, routing_key)
