import redis
import json

class RedisQueue:
    def __init__(self):
        self.r = redis.Redis()

    def publish(self, msg: dict):
        data = json.dumps(msg)
        self.r.lpush('task_1', data)
    
    def consume(self):
        out_queue = self.r.rpop('task_1')
        data = json.loads(out_queue.decode())
        return data

if __name__ == '__main__':
    q = RedisQueue()
    q.publish({'a': 1})
    q.publish({'b': 2})
    q.publish({'c': 3})

    assert q.consume() == {'a': 1}
    assert q.consume() == {'b': 2}
    assert q.consume() == {'c': 3}
