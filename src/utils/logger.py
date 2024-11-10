# utils/logger.py

import logging
import os

class Logger:
    def __init__(self, log_file='app.log', log_level=logging.INFO):
        """Initialize the logger with a specified log file and log level."""
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)

        # Create file handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)

        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)

        # Create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        """Return the configured logger."""
        return self.logger
