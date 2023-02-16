import os
import logging
from logging.handlers import TimedRotatingFileHandler


def logger_loader() -> None:
    _logger_folder_name = os.environ.get("LOGGER_FOLDER_NAME")
    _logger_file_name = os.environ.get("LOGGER_FILE_NAME")
    _logger_dir_name = os.path.join(_logger_folder_name, _logger_file_name)
    _logger_backup_count = int(os.environ.get("LOGGER_BACKUP_COUNT"))
    _logger_name = os.environ.get("LOGGER_NAME")
    _logger_handler = logging.handlers.TimedRotatingFileHandler(
        filename=_logger_dir_name,
        when="D",
        backupCount=_logger_backup_count
    )
    _log_format = logging.Formatter(fmt=(
        '%(asctime)s:\t'
        '%(levelname)s:\t'
        '%(filename)s:'
        '%(funcName)s():'
        '%(lineno)d\t'
        '%(message)s'
    ))
    _logger = logging.getLogger(_logger_name)
    _logger_handler.setFormatter(_log_format)
    _logger.addHandler(_logger_handler)
    _logger.setLevel(logging.ERROR)
    pass
