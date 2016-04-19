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

    def get(self, key):
        '''
        Retrieves a Result instance from storage
        '''
        raise NotImplementedError

    def set(self, key, result):
        '''
        Persist a result onto the underlying storage
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

    def list(self):
        '''
        Returns a list of mismatches
        '''
        raise NotImplementedError
