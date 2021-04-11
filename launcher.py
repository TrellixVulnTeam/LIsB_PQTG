import asyncore
import logging

from schema import SchemaError

from spamfilter import SpamFilter, configuration

try:
    # Looad initial configurations
    server_conf = configuration.load_server_config()
    configuration.config_logging(server_conf)
    # Launch SpamFilter
    SpamFilter(server_conf)
    asyncore.loop()
except SchemaError as e:
    logging.error(f"There was a syntax error in one of the configuration files:\n{e}")
except Exception as e:
    logging.error(f"An unexpected error occured:\n{e}")