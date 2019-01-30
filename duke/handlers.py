from response import Response

class RouteNotFound(Exception):
    pass

def dispatch_route(request, routes):
    for route in routes:
        if request.path == route.path:
            return route.view(request)
    raise RouteNotFound

def handle_request(request, routes):
    try:
        return dispatch_route(request, routes)
    except RouteNotFound:
        return Response(body="Not Found", status_code=404)