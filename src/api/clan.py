
class LazyLoadable(object):
    ''' trait for lazy load
    '''
    def __init(self):
        self.__loaded = False

    def fetch(self):
        raise NotImplementedError

    def ready(self):
        return self.__loaded

class Build(object):
    ''' build info
    '''
    pass


class Play(object, LazyLoadable):
    ''' play info
    '''
    
    def __init__(self, pid, name):
        self._id = pid
        self._name = name
        self._level = None
        self._builds = []

    def __iter__(self):
        return self._builds.__iter__()

class clan(object, LazyLoadable):
    ''' clan info
    '''
    def __init__(self, name, kargs*, kwargs**):
        self._name = name
        self._id = None
        self._desc = None
        self._plays = []

    def __iter__(self):
        return self._plays.__iter__()

