import bottle


def create(function, Class):
    def f():
        o = Class.FromDict(bottle.request.json)
        print(o.to_json())
        if o is None:
            raise bottle.HTTPError(400)
        result = function(o)
        return result.to_dict()
    return f


def fetch(function):
    def f(id):
        if id is None:
            raise bottle.HTTPError(400)
        result = function(id)
        return result.to_dict()
    return f
