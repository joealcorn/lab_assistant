from lab_assistant.storage.backends.base import StorageBackend
from lab_assistant.storage.backends.null import NullBackend
from lab_assistant.storage.backends.redis import RedisBackend
from lab_assistant.tests import cases
import lab_assistant


class FakeStorage(StorageBackend):
    pass


class TestGetStorage(cases.TestCase):
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


class TestRedisBackend(cases.RedisTestCase):
    storage_class = 'lab_assistant.storage.backends.redis.RedisBackend'

    def storage(self):
        return lab_assistant.storage.get_storage(self.storage_class)

    def test_get_nonexistent(self):
        assert self.storage().get(123456) is None

    def test_set_and_get(self):
        storage = self.storage()
        storage.set(123456, 'fake_result')
        assert storage.get(123456) == 'fake_result'

    def test_set_and_list(self):
        storage = self.storage()
        storage.set(123456, 'fake_result')
        assert list(storage.list()) == ['fake_result']

    def test_set_and_remove(self):
        storage = self.storage()
        storage.set(123456, 'fake_result')
        assert storage.get(123456) == 'fake_result'
        storage.remove(123456)
        assert storage.get(123456) is None

    def test_set_and_clear_and_list(self):
        storage = self.storage()
        storage.set(123456, 'fake_result')
        assert list(storage.list()) == ['fake_result']
        storage.clear()
        assert list(storage.list()) == []
