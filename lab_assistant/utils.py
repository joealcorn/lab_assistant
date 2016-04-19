from importlib import import_module


def import_path(path):
    module_path, object_name = path.rsplit('.', 1)
    module = import_module(module_path)
    return getattr(module, object_name)


def cached_property(func):
    def inner(*a, **kw):
        if hasattr(inner, '_value'):
            return inner._value
        setattr(inner, '_value', func(*a, **kw))
        return inner._value
    return property(inner)
