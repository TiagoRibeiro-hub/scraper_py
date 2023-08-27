import os
from dotenv import dotenv_values

config = {
    **dotenv_values('.env.shared'),
    **dotenv_values('.env.secret'),
    # **os.environ
}

ZUMUB_EMAIL = config['ZUMUB_EMAIL']
ZUMUB_PASSWORD = config['ZUMUB_PASSWORD']
SCRAPEOPS_IO_API_KEY = config['SCRAPEOPS_IO_API_KEY']
REDIS_PASS = config['REDIS_PASS']

