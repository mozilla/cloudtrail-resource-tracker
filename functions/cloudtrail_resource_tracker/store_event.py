import logging
from .config import CONFIG

logger = logging.getLogger()
logging.getLogger().setLevel(CONFIG.log_level)


def store_event(event):
    # Construct and write an event to the DB based
    logger.info('Event to be written to the DB is : {}'.format(event))

    # TODO : Add the code to write the data to the data store
