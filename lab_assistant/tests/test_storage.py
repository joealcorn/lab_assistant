from lab_assistant.storage.backends.base import StorageBackend
from lab_assistant.storage.backends.null import NullBackend
from lab_assistant.storage.backends.redis import RedisBackend
from lab_assistant.tests.cases import TestCase
import lab_assistant


class FakeStorage(StorageBackend):
    pass


class TestGetStorage(TestCase):
    def test_get_default_storage(self):
        storage = lab_assistant.storage.get_storage()
        assert isinstance(storage, NullBackend)

        lab_assistant.conf.storage.update({
            'path': 'lab_assistant.storage.backends.redis.RedisBackend'
        })

        storage = lab_assistant.storage.get_storage()
        assert isinstance(storage, RedisBackend)

    def test_same_instance_returned_multiple_calls(self):
        first = lab_assistant.storage.get_storage()
        second = lab_assistant.storage.get_storage()
        assert id(first) == id(second)

    def test_get_custom_storage(self):
        path = 'lab_assistant.tests.test_storage.FakeStorage'
        storage = lab_assistant.storage.get_storage(path, test=True)
        assert isinstance(storage, FakeStorage)
        assert storage.kwargs['test']
