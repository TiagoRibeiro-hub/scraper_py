from constants import BLOCK_RESOURCE_NAMES, BLOCK_RESOURCE_TYPES

class Interceptor:
    def block(route):
        # * intercept all requests and abort blocked ones
        if route.request.resource_type in BLOCK_RESOURCE_TYPES:
            return route.abort()
        if any(key in route.request.url for key in BLOCK_RESOURCE_NAMES):
            return route.abort()
        return route.continue_()
      
    def request(request):
      print("REQUEST: ", request)
      return request
    
    def response(response):
      print("RESPONSE ", response)
      return response
    