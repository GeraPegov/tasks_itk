class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


class MetaSingleton(type):
    _instance: dict = {}

    def __call__(cls, *args, **kwrgs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, *kwrgs)
        return cls._instance[cls]
