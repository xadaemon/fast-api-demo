from walrus import Walrus
from lib.config import settings

datastore = Walrus(host=settings.get("data.redis.host"),
                   port=settings.get("data.redis.port"),
                   db=settings.get("data.redis.db"))
