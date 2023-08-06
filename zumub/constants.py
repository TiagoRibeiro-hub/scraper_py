from enviroment import SCRAPEOPS_IO_API_KEY

# ! GLOBAL
BASE_URL = 'https://www.zumub.com/EN/'
ZUMBU = 'zumbu'
PAGE_EQUALS = '?page='

# ! BLOCKERS
# * block pages by resource type.
BLOCK_RESOURCE_TYPES = [
  'beacon',
  'csp_report',
  'font',
  'image',
  'imageset',
  'media',
  'object',
  'texttrack',
]
# * block popular 3rd party resources like tracking and advertisements.
BLOCK_RESOURCE_NAMES = [
  'adzerk',
  'analytics',
  'cdn.api.twitter',
  'doubleclick',
  'exelator',
  'facebook',
  'fontawesome',
  'google',
  'google-analytics',
  'googletagmanager',
]

SCRAPEOPS_IO_API_KEY = SCRAPEOPS_IO_API_KEY
SCRAPEOPS_NUM_RESULTS = 10