import re
import random
import os
import json
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
    """returns string to camel caps

    Example
    to_camel('foo_bar') == 'FooBar'
    """
    return str(s.title().replace('_', ''))
    # assume the titles are ascii, else class name fail
    # "%s doesn't convert to a good string for a class name" % s)
