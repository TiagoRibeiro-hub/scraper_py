import os
from dotenv import dotenv_values

# ! CONFIG
config = {
    **dotenv_values('.env.shared'),
    **dotenv_values('.env.secret'),
    # **os.environ
}

# ! ZUMUB
ZUMUB_EMAIL = config['ZUMUB_EMAIL']
ZUMUB_PASSWORD = config['ZUMUB_PASSWORD']

# ! SCRAPEOPS
SCRAPEOPS_IO_API_KEY = config['SCRAPEOPS_IO_API_KEY']

# ! REDIS
REDIS_ENV = {
    'HOST_REDIS': config['HOST_REDIS'],
    'PORT_REDIS': config['PORT_REDIS'],
    'REDIS_PASS': config['REDIS_PASS'],
}

