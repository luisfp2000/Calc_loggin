import logging

class CustomLogging:
    def __init__(self, logger_name, log_file):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)
        
        formatter = logging.Formatter('%(asctime)s:%(name)s:%(module)s:%(levelname)s:%(message)s')
        
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        
        self.logger.addHandler(file_handler)
        
        stream_handler = logging.StreamHandler()  # Create a StreamHandler
        stream_handler.setFormatter(formatter)   # Set the same formatter as the file handler
        
        self.logger.addHandler(stream_handler)    # Add the stream handler to the logger
    
    def get_logger(self):
        return self.logger