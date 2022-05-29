import functools
import shutil


def required(func_validation: object) -> object:
    def decorator(func):
        @functools.wraps(func)
        def result(*args, **kwargs):
            if not func_validation():
                return
            func(*args, **kwargs)
        return result
    return decorator


def validate_adb_exists() -> bool:
    return not shutil.which('adb') is None
