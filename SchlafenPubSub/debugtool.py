import click
from SchlafenPubSub.consumer import subscriber, subscriber_topic, subscriber_routing
from SchlafenPubSub.producer import publisher, publisher_topic, publisher_routing


@click.command()
@click.option('--exchange')
@click.option('--model', default='fanout')
@click.option('--routing_key', default='None')
@click.option('--user', default='admin')
@click.option('--password', default='admin')
@click.option('--host', default='127.0.0.1')
@click.option('--vhost', default='/')
@click.option('--port', default=5672)
@click.option('--durable', default=False)
def debug_sub(exchange, model, routing_key, user, password, host, vhost, port, durable):
    if model == 'fanout':
        subscriber(host=host, port=port, user=user, password=password,
                   exchange=exchange, vhost=vhost).start()
    elif model == 'direct':
        subscriber_routing(host=host, port=port, user=user, password=password,
                           exchange=exchange, vhost=vhost, routing_key=routing_key, durable=durable).start()
    elif model == 'topic':
        subscriber_topic(host=host, port=port, user=user, password=password,
                         exchange=exchange, vhost=vhost, routing_key=routing_key, durable=durable).start()


@click.command()
@click.option('--exchange')
@click.option('--model', default='fanout')
@click.option('--routing_key', default='None')
@click.option('--user', default='admin')
@click.option('--password', default='admin')
@click.option('--host', default='127.0.0.1')
@click.option('--vhost', default='/')
@click.option('--port', default=5672)
@click.option('--content', default='hello')
@click.option('--durable', default=False)
def debug_pub(exchange, model, routing_key, user, password, host, vhost, port, content, durable):
    if model == 'fanout':
        publisher(host=host, port=port, user=user, password=password,
                  exchange=exchange, vhost=vhost, durable=durable).pub(content)
    elif model == 'direct':
        print(routing_key)
        publisher_routing(host=host, port=port, user=user, password=password,
                          exchange=exchange,  vhost=vhost, routing_key=routing_key, durable=durable).pub(content, routing_key=routing_key)
    elif model == 'topic':
        publisher_topic(host=host, port=port, user=user, password=password,
                        exchange=exchange,  vhost=vhost, routing_key=routing_key, durable=durable).pub(content, routing_key=routing_key)