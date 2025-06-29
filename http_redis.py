import random
import time
import redis

class RateLimitExceed(Exception):
    pass

r = redis.Redis()
class RateLimiter:
    def test(self) -> bool:
        now = time.time()
        r.zremrangebyscore('request', '-inf', now - 3)
        r.zadd('request', {str(now): now})
        print(r.zrange('request', 0, -1))
        return r.zcard('request') <= 5 
        
        


def make_api_request(rate_limiter: RateLimiter):
    if not rate_limiter.test():
        raise RateLimitExceed
    else:
        # какая-то бизнес логика
        pass


if __name__ == '__main__':
    rate_limiter = RateLimiter()

    for _ in range(50):
        time.sleep(random.randint(1, 2))

        try:
            make_api_request(rate_limiter)
        except RateLimitExceed:
            print("Rate limit exceed!")
        else:
            print("All good")
