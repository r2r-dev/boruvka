from json import loads


def jsonize(func):
    def wrap(self, *args, **kwargs):
        payload = kwargs['payload']
        if isinstance(
                payload,
                basestring,
        ):
            kwargs['payload'] = loads(payload)
        return func(self, *args, **kwargs)
    return wrap


class BoruvkaBaseApi(object):
    def __init__(self, dao):
        self._dao = dao


class BoruvkaApiException(Exception):
    pass