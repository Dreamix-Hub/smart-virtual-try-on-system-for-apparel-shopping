# test_redis_connection.py
import redis
import config

r = redis.from_url(config.settings.REDIS_URL.get_secret_value(), decode_responses=True)

r.set("test_key", "hello")
print(r.get("test_key"))  # should print: hello

r.delete("test_key")