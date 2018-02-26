import logging
from logging.handlers import RotatingFileHandler

default_log_dir = "app.logs"
log_backup_count = 0
max_log_file_bytes = 512
console_format_str = "%(asctime)s %(levelname)s %(message)s"
date_formatter_str = '[%Y-%m-%d %H:%M:%S]'
console_formatter = logging.Formatter(console_format_str, datefmt=date_formatter_str)


def init_base_log(logger, log_dir):
    base_handler = RotatingFileHandler(log_dir, mode='a', maxBytes=max_log_file_bytes,
                                       encoding="utf-8", backupCount=log_backup_count)
    base_handler.setFormatter(console_formatter)
    base_handler.setLevel(logging.INFO)
    logger.addHandler(base_handler)


def init_console_log(logger):
    console = logging.StreamHandler()
    console.setFormatter(console_formatter)
    logger.addHandler(console)


def init_log(log_dir=None):
    root_logger = logging.getLogger("")
    root_logger.setLevel(logging.INFO)

    if log_dir:
        init_base_log(root_logger, log_dir)
    else:
        init_base_log(root_logger, default_log_dir)
    init_console_log(root_logger)
