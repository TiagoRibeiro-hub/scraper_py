from enviroment import SCRAPEOPS_IO_API_KEY

# ! ZUMUB
BASE_URL = 'https://www.zumub.com/EN/'

ZUMBU = 'zumbu'
SORT_BY_NAME = 'sort=2a'
PAGE_EQUALS = 'page='
PAGE_ACTIVE_COUPONS = 'active_coupons_page'
PAGE_BRANDS = 'brands'
# * Files
ZUMUB_DATA_PATH = 'scrape/zumub/data/'
ZUMUB_COOKIES_PATH = 'scrape/zumub/data/cookies'

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

# ! SCRAPEOPS IO
SCRAPEOPS_IO_API_KEY = SCRAPEOPS_IO_API_KEY
SCRAPEOPS_NUM_RESULTS = 10
