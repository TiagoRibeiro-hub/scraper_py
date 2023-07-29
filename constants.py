
# ! GLOBAL
BASE_URL = 'https://www.zumub.com/EN/'
ZUMBU = 'zumbu'

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

