import pika
from SchlafenPubSub.setting import schlafen_pubsub_ip, schlafen_pubsub_port, schlafen_pubsub_user, \
    schlafen_pubsub_password


class base_pub_sub():
    """
    基于BlockingConnection消息中间件的基类
    1. 创建connection
    2. 创建channel 一个channel对应1个exchange
    3. 默认 exchange_name exchange_type routing_key等属性

    publisher发消息(生产者)——> 消息队列[exchange交换机——>Routes路由——>Queue队列] ——>consumer收消息(消费者)

    ·Publisher: 生产者，发布消息到MQ中的
    ·Consumer：消费者，从MQ中接收消息的
    ·Exchange：交换机，建立生产者和队列之间联系
    ·Queue：队列，存储消息的
    ·Routes：路由，交换机以什么样的策略将消息发送给队列


    封装
    1. 重链接
    2. 断开


    todo: based on non-blocking adapters
    """

    def __init__(self, host=schlafen_pubsub_ip, port=schlafen_pubsub_port, user=schlafen_pubsub_user,
                 password=schlafen_pubsub_password, channel_number=1, queue_name='', routing_key='default', exchange='',
                 exchange_type='fanout', vhost='/'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.queue_name = queue_name
        self.exchange = exchange
        self.routing_key = routing_key
        self.vhost = vhost
        self.exchange_type = exchange_type
        self.channel_number = channel_number

        self.credentials = pika.PlainCredentials(
            self.user, self.password, erase_on_connect=True)
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host, port=self.port, virtual_host=self.vhost,
                                      credentials=self.credentials, heartbeat=15, socket_timeout=5,
                                      )
        )

        self.channel = self.connection.channel(
            channel_number=self.channel_number)

    def reconnect(self):
        try:
            self.connection.close()
        except:
            pass

        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host, port=self.port,credentials=self.credentials,
                                      heartbeat=15, virtual_host=self.vhost,
                                      socket_timeout=5,))
        self.channel = self.connection.channel(
            channel_number=self.channel_number)
        return self

    def close(self):
        self.connection.close()
