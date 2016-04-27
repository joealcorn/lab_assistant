from unittest import TestCase as _TestCase
from redis import StrictRedis
import exam

from lab_assistant.utils import cached_property
import lab_assistant


class TestCase(exam.cases.Exam, _TestCase):
    @exam.before
    def reset_config(self):
        lab_assistant.conf.storage = {
            'path': 'lab_assistant.storage.backends.null.NullBackend',
            'options': {},
        }


class RedisTestCase(TestCase):
    @exam.before
    def clear_redis(self):
        self.redis.flushdb()

    @cached_property
    def redis(self):
        return StrictRedis()
