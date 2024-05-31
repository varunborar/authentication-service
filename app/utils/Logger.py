import logging
import sys
import datetime
import os
import uuid

from .env import env


class Logger:

    def __init__(self, name='root', formatString=None):
        self._logger = None
        self._id = str(uuid.uuid4())
        self.name = name + f'[{self._id[:4]}]'
        if formatString is None:
            self.formatter = logging.Formatter('[%(asctime)s] %(name)s : %(levelname)s - %(message)s')
        else:
            self.formatter = logging.Formatter(formatString)

    def addFileHandler(self, pathToLogFolder, level=logging.DEBUG):
        if not os.path.exists(f'{pathToLogFolder}/logs'):
            os.makedirs(f'{pathToLogFolder}/logs')
        fileHandler = logging.FileHandler(f'{pathToLogFolder}/logs/{datetime.datetime.now().strftime("%Y-%m-%d")}.log')
        fileHandler.setLevel(level)
        fileHandler.setFormatter(self.formatter)
        self._logger.addHandler(fileHandler)

    def addConsoleHandler(self, level=logging.INFO):
        consoleHandler = logging.StreamHandler(sys.stdout)
        consoleHandler.setLevel(level)
        consoleHandler.setFormatter(self.formatter)
        self._logger.addHandler(consoleHandler)

    def configure(self, name=None, level=logging.DEBUG, enableConsoleHandler=True, enableFileHandler=False,
                  pathToLogFolder='temp'):
        logger = logging.getLogger(name if name is not None else self.name)
        logger.setLevel(level)
        self._logger = logger

        if enableConsoleHandler:
            self.addConsoleHandler(level)
        if enableFileHandler:
            self.addFileHandler(pathToLogFolder)

    def info(self, logname, logMessage=""):
        self._logger.info(f'logName={logname} {f"{logMessage}" if logMessage != "" else ""}')

    def debug(self, logname, logMessage=""):
        self._logger.debug(f'logName={logname} {f"{logMessage}" if logMessage != "" else ""}')

    def error(self, logname, logMessage=""):
        self._logger.error(f'logName={logname} {f"{logMessage}" if logMessage != "" else ""}')

    def warning(self, logname, logMessage=""):
        self._logger.warning(f'logName={logname} {f"{logMessage}" if logMessage != "" else ""}')


logger = Logger()
logger.configure(
    name=env.get('SOURCE', 'root'),
    level=logging.DEBUG,
    enableConsoleHandler=True,
    enableFileHandler=False
)
