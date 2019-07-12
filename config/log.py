import logging
from logging.handlers import RotatingFileHandler


class Log:
    level = logging.INFO
    file_log_handler = RotatingFileHandler("./log/log.log", maxBytes=1024 * 1024 * 100, backupCount=10)
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')


def set_log():
    logging.basicConfig(level=Log.level)
    file_log_handler = Log.file_log_handler
    file_log_handler.setFormatter(Log.formatter)
    logging.getLogger().addHandler(file_log_handler)
