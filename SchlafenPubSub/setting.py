import os
schlafen_pubsub_ip = os.getenv('SCHLAFEN_PUBSUB_IP', 'localhost')
schlafen_pubsub_port = os.getenv('SCHLAFEN_PUBSUB_PORT', 5672)
schlafen_pubsub_user = os.getenv('SCHLAFEN_PUBSUB_USER', 'guest')
schlafen_pubsub_password = os.getenv('SCHLAFEN_PUBSUB_PWD', 'guest')
