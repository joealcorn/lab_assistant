from copy import deepcopy
import pickle

from simpleflake import simpleflake

from lab_assistant import conf, utils


__all__ = [
    'get_storage',
    'store',
    'retrieve',
    'retrieve_all',
    'clear',
]


def get_storage(path=None, name='Experiment', **opts):
    if not path:
        path = conf.storage['path']
        _opts = deepcopy(conf.storage.get('options', {}))
        _opts.update(opts)
        opts = _opts

    if path in get_storage._cache:
        return get_storage._cache[path]

    Storage = utils.import_path(path)
    get_storage._cache[path] = Storage(name, **opts)
    return get_storage._cache[path]
get_storage._cache = {}


def store(result, storage=None):
    storage = storage or get_storage()
    key = simpleflake()
    storage.set(key, result)
    return key


def retrieve(key, storage=None):
    storage = storage or get_storage()
    return storage.get(key)


def retrieve_all(storage=None):
    return (storage or get_storage()).list()


def remove(key, storage=None):
    (storage or get_storage()).remove(key)


def clear(storage=None):
    return (storage or get_storage()).clear()
