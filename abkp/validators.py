import functools


def required(func_validation):
    def decorator(func):
        @functools.wraps(func)
        def result(*args, **kwargs):
            if not func_validation():
                return
            func(*args, **kwargs)
        return result
    return decorator
