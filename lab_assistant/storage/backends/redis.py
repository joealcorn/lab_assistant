from __future__ import absolute_import

from redis import StrictRedis

from lab_assistant.storage.backends.base import StorageBackend
from lab_assistant.utils import cached_property


class RedisBackend(StorageBackend):

    def validate_kwargs(self, kwargs):
        kwargs.setdefault('connection_uri', '')

    @cached_property
    def conn(self):
        return StrictRedis.from_url(self.kwargs['connection_uri'])

    @property
    def _key(self):
        return 'results:%s' % self.experiment_key

    def _retrieve(self, key):
        val = self.conn.zrangebyscore(self._key, key, key)
        if val:
            return val[0]
        return None

    def _persist(self, key, result):
        self.conn.zadd(self._key, key, result)

    def _retrieve_many(self, limit):
        if limit is None or limit is 0:
            limit = -1
        return self.conn.zrevrange(self._key, 0, limit)

    def remove(self, key):
        self.conn.zremrangebyscore(self._key, key, key)

    def clear(self):
        self.conn.zremrangebyrank(self._key, 0, -1)
