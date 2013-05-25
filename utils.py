import re
import random

class Dotable(dict):
    __getattr__= dict.__getitem__
    def __init__(self, d=None):
        if isinstance(d, Dotable):
            return d
        if d is None:
            d = {}
        dict.update(self, **dict((k, self.parse(v)) for k, v in d.iteritems()))
    def parse(self, v):
        if isinstance(v, dict): return Dotable(v)
        elif isinstance(v, list): return [self.parse(i) for i in v]
        else: return v
    #def update(self, **d):
    #   d = Dotable(d)
    #   super(Dotable, self).update(**d)

def to_camel(s):
    """returns string to camel caps

    Example
    to_camel('foo_bar') == 'FooBar'
    """
    try:
        return s.title().replace('_', '').encode('ascii')
    except Exception:  # TODO specify which kind of error
        raise ValueError("%s doesn't convert to a good string for a class name" % kname)
                

def format_(s, _locals=None):
    # first replace #s with digits then fill in rest using _locals
    def callback(matchobj):
        return '%s' % random.randrange(10)
    s = re.sub(r'#', callback, s)
    return s