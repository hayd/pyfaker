from collections import Mapping
import json
import os
from string import Formatter


class CallFormatter(Formatter):

    def get_field(self, field_name, *args, **kwargs):
        obj, used_key = Formatter.get_field(self, field_name, *args, **kwargs)
        return obj(), used_key
call_fmt = CallFormatter()


def get_locales():
    def curpath():
        pth, _ = os.path.split(os.path.abspath(__file__))
        return pth
    fpath = os.path.join(curpath(), 'locales.json')
    with open(fpath, 'r') as f:
        return json.load(f)
# _all_locales = get_locales()


def to_camel(s):
    """returns string to camel caps.

    Example
    to_camel('foo_bar') == 'FooBar'

    """
    # assume the titles are ascii, else class name fail
    # "%s doesn't convert to a good string for a class name" % s)
    return str(s.title().replace('_', ''))


def recursive_update(d, u):
    "Update dict d recursively with values from dict u."
    for k, v in u.items():
        if isinstance(v, Mapping):
            r = recursive_update(d.get(k, {}), v)
            d[k] = r
        elif isinstance(v, list):
            d[k] = d.get(k, []) + v
        else:
            d[k] = u[k]
    return d
