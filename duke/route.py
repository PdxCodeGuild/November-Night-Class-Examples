class Route:
    def __init__(self, path, view):
        self.path = path
        self.view = view

def route(*args, **kwargs):
    return Route(*args, **kwargs)