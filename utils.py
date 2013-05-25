import re
import random


def unruby(json_):
    if isinstance(json_, basestring):
        # TODO replace all #{foo_bar.baz} with {FooBar.baz}, may not be needed
        return re.sub('#({[^}]*})', r'\1', json_)
    if isinstance(json_, list):
        return map(unruby, json_)
    if isinstance(json_, dict):
        return dict((k, unruby(v)) for k, v in json_.items())
    return json_


def to_camel(s):
    """returns string to camel caps

    Example
    to_camel('foo_bar') == 'FooBar'
    """
    try:
        return s.title().replace('_', '').encode('ascii')
    except Exception:  # TODO specify which kind of error
        raise ValueError(
            "%s doesn't convert to a good string for a class name" % kname)


def format_(s, _locals=None):
    # first replace #s with digits then fill in rest using _locals
    def callback(matchobj):
        return '%s' % random.randrange(10)
    s = re.sub(r'#', callback, s)
    return s
