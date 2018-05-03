from functools import wraps


class Log:
    def __init__(self, logger):
        self.logger = logger

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            self.logger.info('{}'.format(result))
            return result

        return wrapper
