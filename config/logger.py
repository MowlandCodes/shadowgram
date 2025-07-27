import logging
import time

from colorama import Fore, Style


class FileFormatter(logging.Formatter):
    format = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] - %(name)s - [%(levelname)s]: %(message)s"
    datefmt = "%d-%b-%Y %H:%M:%S"

    FORMATS = {
        logging.DEBUG: f"{format}",
        logging.INFO: f"{format}",
        logging.WARNING: f"{format}",
        logging.ERROR: f"{format}",
        logging.CRITICAL: f"{format}",
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, self.datefmt)
        return formatter.format(record)


class ConsoleFormatter(logging.Formatter):
    debug = Fore.WHITE
    informative = Fore.BLUE
    warning = Fore.YELLOW
    error = Fore.RED
    critical = Fore.RED + Style.BRIGHT
    format = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] - %(name)s - [%(levelname)s]: %(message)s"
    datefmt = "%d-%b-%Y %H:%M:%S"

    FORMATS = {
        logging.DEBUG: f"{debug}{format}{Style.RESET_ALL}",
        logging.INFO: f"{informative}{format}{Style.RESET_ALL}",
        logging.WARNING: f"{warning}{format}{Style.RESET_ALL}",
        logging.ERROR: f"{error}{format}{Style.RESET_ALL}",
        logging.CRITICAL: f"{critical}{format}{Style.RESET_ALL}",
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, self.datefmt)
        return formatter.format(record)


# Initializing Logger
log_gram = logging.getLogger("Shadowgram")

# For debug purpose (change to logging.WARNING for production)
log_gram.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(ConsoleFormatter())
file_handler = logging.FileHandler("shadowgram.log")
file_handler.setFormatter(FileFormatter())

log_gram.addHandler(file_handler)  # For File logging
log_gram.addHandler(stream_handler)  # For Console logging
