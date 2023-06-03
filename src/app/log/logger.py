import json
import datetime
import os

class Logger:
    INFO = 1
    WARNING = 2
    ERROR = 3
    DEBUG = 4

    def __init__(self, ambiente):
        self._ambiente = ambiente

    def _log(self, message, level, break_line):
        type = {
            self.INFO: 'INFO',   
            self.WARNING: 'WARNING',  
            self.ERROR: 'ERROR',   
            self.DEBUG: 'DEBUG' 
        }

        if level not in type:
            raise ValueError(f"Nivel invalido (usar entre 1 e 4): {level}")

        current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        log_data = {
           type[level]: level,
            "message": message,
            "ambiente": self._ambiente,
            "timestamp": current_time,
            
        }

        log_string = json.dumps(log_data)
        log_string = " " + log_string if break_line else log_string

        print(log_string)

    def info(self, message, break_line=False):
        self._log(message, self.INFO, break_line)

    def warning(self, message, break_line=False):
        self._log(message, self.WARNING, break_line)

    def error(self, message, break_line=False):
        self._log(message, self.ERROR, break_line)

    def debug(self, message, break_line=False):
        self._log(message, self.DEBUG, break_line)
        

"""Exemplo de uso:

from log.logger import Logger

logger = Logger(__name__)

logger.warning("WARN")
logger.info("INFO")
logger.error("ERROR")
logger.debug("DEBUG")

"""

        