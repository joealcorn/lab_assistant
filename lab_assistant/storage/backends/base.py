import pickle


class StorageBackend(object):
    '''
    This defines the API for storage all storage backends.
    '''

    def __init__(self, experiment_key, **kwargs):
        self.experiment_key = experiment_key
        self.kwargs = kwargs
        self.validate_kwargs(kwargs)

    def validate_kwargs(self, kwargs):
        return

    def serialize(self, result):
        return pickle.dumps(result)

    def deserialize(self, data):
        return pickle.loads(data)

    def get(self, key):
        '''
        Retrieves a Result instance from storage
        '''
        data = self._retrieve(key)
        if data:
            return self.deserialize(data)

    def set(self, key, result):
        '''
        Persist a result onto the underlying storage
        '''
        self._persist(key, self.serialize(result))

    def list(self, limit=25):
        '''
        Returns a list of all results
        '''
        return [self.deserialize(r) for r in self._retrieve_many(limit)]

    # All methods below should be implemented by subclasses

    def _retrieve(self, key):
        '''
        Retrieves the serialized form of a Result from storage
        '''
        raise NotImplementedError

    def _persist(self, key, data):
        '''
        Does the actual persistance of a result onto the underlying storage
        '''
        raise NotImplementedError

    def _retrieve_many(self, limit):
        '''
        Retrieves a list of the serialized form of all results
        '''
        raise NotImplementedError

    def remove(self, key):
        '''
        Remove a single result
        '''
        raise NotImplementedError

    def clear(self):
        '''
        Remove all results
        '''
        raise NotImplementedError
