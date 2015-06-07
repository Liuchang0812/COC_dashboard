from tornado.gen import Future, coroutine, Return
try:
    import json
except NotImplementedError:
    import simplejson as json

import requests

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


class Play(LazyLoadable):
    ''' play info
    '''
    
    def __init__(self, pid, name):
        self._id = pid
        self._name = name
        self._level = None
        self._builds = []

    def __iter__(self):
        return self._builds.__iter__()

class clan(LazyLoadable):

    ''' clan info
    '''
    def __init__(self, name, *kargs, **kwargs):
        self._name = name
        self._id = None
        self._desc = None
        self._plays = []

    def __iter__(self):
        return self._plays.__iter__()

class service(object):

    base_url = "http://core-clashofclans.cf/json/reply/"
    @classmethod
    @coroutine
    def search(cls, name):
        try:
            req = {'Tag':'', 'Search':name}
            url = cls.base_url + "ClanSearch"
            res = requests.post(url, data=json.dumps(req))
            clanid = res.json()[0]['ClanID']

            req = {'Id':clanid}
            url = cls.base_url + "Clan"
            res = requests.post(url, data=json.dumps(req))
            Return(res.json())
        except requests.Timeout:
            Return(None)

