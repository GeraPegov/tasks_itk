import redis
r = redis.Redis()

def single(max_processing_time):
    def single(func):
        r = redis.Redis()
        lock = r.set('blocked', '1', nx=True, ex=max_processing_time)
        def wrapper(*args, **kwargs):
            if lock:
                func(*args, **kwargs)
            else:
                print(f'Wait {r.ttl('blocked')}')
        return wrapper
    return single

