import re
import random
import os
import json
from string import Formatter


class BaseFake(object):
    pass


class CallFormatter(Formatter):
    def get_field(self, field_name, *args, **kwargs):
        obj, used_key = Formatter.get_field(self, field_name, *args, **kwargs)
        return obj(), used_key

'''
class CallFormatter(Formatter):
    def get_field(field_name, *args, **kwargs):
        used_key = Formatter.get_field(field_name, *args, **kwargs)
        return (used_key[0](),) + used_key[1:]



class CallFormatter(Formatter):
    def get_field(self, field_name, *args, **kwargs):
        if kwargs is None:
            kwargs = kwargs.update(args[1])
        else:
            kwargs.update(args[1])
        obj, used_key = Formatter.get_field(self, field_name, args[0:1], kwargs)
        return obj(kwargs['cls']()), used_key
'''
call_fmt = CallFormatter()


def get_locales():
    def curpath():
        pth, _ = os.path.split(os.path.abspath(__file__))
        return pth
    fpath = os.path.join(curpath(), 'locales.json')
    with open(fpath, 'r') as f:
        return json.load(f)
_all_locales = get_locales()


def to_camel(s):
    """returns string to camel caps

    Example
    to_camel('foo_bar') == 'FooBar'
    """
    try:
        return s.title().replace('_', '').encode('ascii')
    except Exception:  # TODO specify which kind of error
        raise ValueError(
            "%s doesn't convert to a good string for a class name" % s)

def update_loc(loc1, loc2):
    loc1.update(loc2)

'''
def format_(s, current, fake_=None):
    namespace = dict(current.__dict__, **{'cls': current}) # and fake_ ?
    # first replace #s with digits then fill in rest using _locals
    def callback(matchobj):
        return '%s' % random.randrange(10)
    s = re.sub(r'#', callback, s)

    return s
    fmt = CallFormatter()
    return fmt.format(s, **namespace)
'''
