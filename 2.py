import logging
from logging import handlers

logger = logging.getLogger()

handler = handlers.SysLogHandler(address=("192.168.203.33", 514))
logger.addHandler(handler)

logger.info("hello there")
