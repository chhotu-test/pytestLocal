import logging
import os
from datetime import datetime


class Logger:
    
    @staticmethod
    def setup_logger(name: str = "test_logger", log_level=logging.INFO):
        logger = logging.getLogger(name)
        logger.setLevel(log_level)
        
        if not logger.handlers:
            log_dir = "logs"
            os.makedirs(log_dir, exist_ok=True)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            log_file = os.path.join(log_dir, f"test_log_{timestamp}.log")
            
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(log_level)
            
            console_handler = logging.StreamHandler()
            console_handler.setLevel(log_level)
            
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)
            
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)
        
        return logger
    
    @staticmethod
    def get_logger(name: str = "test_logger"):
        return logging.getLogger(name)
