import logging
import os

LOGGING_LEVEL = logging.INFO  # например, или DEBUG, WARNING, ERROR
LOGGING_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
LOG_FILE_PATH = os.path.join(os.getcwd(), 'logs', 'bot.log')

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': LOGGING_FORMAT
        },
    },
    'handlers': {
        'default': {
            'level': LOGGING_LEVEL,
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': LOG_FILE_PATH,
            'mode': 'a',  # append mode
        },
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['default'],
            'level': LOGGING_LEVEL,
            'propagate': True
        },
    }
}
