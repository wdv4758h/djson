import json
import functools

def request_json(func):
    @functools.wraps(func)
    def wrapper(request, *args, **kwargs):
        request.json = json.loads(request.body)
        return func(request, *args, **kwargs)
    return wrapper
