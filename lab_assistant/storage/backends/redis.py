from __future__ import absolute_import
import time

from redis import StrictRedis

from lab_assistant.storage.backends.base import StorageBackend
from lab_assistant.utils import cached_property


class RedisBackend(StorageBackend):
    def __init__(self, connection_uri=''):
        self._connection_uri = connection_uri

    @cached_property
    def conn(self):
        return StrictRedis.from_url(self._connection_uri)
