from importlib import import_module


def import_path(path):
    module_path, object_name = path.rsplit('.', 1)
    module = import_module(module_path)
    return getattr(module, object_name)
