import logging

class CustomLogging:


    def __init__(self, name, log_level, modulo):

        print(name)
        print(log_level)
        print(modulo)

        self.logger = logging.getLogger(modulo)
        
        filename = f"{name}.log"
        
        if log_level =="INFO":
            self.logger.setLevel(logging.INFO)
        elif log_level =="DEBUG":
            self.logger.setLevel(logging.DEBUG)
        elif log_level =="ERROR":
            self.logger.setLevel(logging.ERROR)
        elif log_level =="WARNING":
            self.logger.setLevel(logging.WARNING)
        elif log_level =="CRITICAL":
            self.logger.setLevel(logging.CRITICAL)
        else:
            self.logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s:%(name)s:%(module)s:%(levelname)s:%(message)s"
        )

        file_handler = logging.FileHandler(filename)

        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()  # Create a StreamHandler
        stream_handler.setFormatter(formatter)   # Set the same formatter as the file handler
        
        self.logger.addHandler(stream_handler)    # Add the stream handler to the logger
    

    
    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)