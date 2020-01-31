import os


class Config:
    def __init__(self):
        self.log_level = os.getenv('LOG_LEVEL')


CONFIG = Config()