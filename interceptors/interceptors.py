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


# block popular 3rd party resources like tracking and advertisements.
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
class Interceptor:
    def block(route):
        # * intercept all requests and abort blocked ones
        if route.request.resource_type in BLOCK_RESOURCE_TYPES:
            return route.abort()
        if any(key in route.request.url for key in BLOCK_RESOURCE_NAMES):
            return route.abort()
        return route.continue_()
      
    def request(request):
      # we can update requests with custom headers
      if "secret" in request.url :
          # request.headers['x-secret-token'] = "123"
          print("patched headers of a secret request")
      # or adjust sent data
      if request.method == "POST":
          print("POST request")
      return request
    
    def response(response):
      # we can extract details from background requests
      if response.request.resource_type == "xhr":
          print("COOKIES ", response.headers)
      return response
    