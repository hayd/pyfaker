import json
import random
from utils import Dotable, to_camel, format_
import re


lang_code = 'en'
lang, sublang = lang_code.split() if '-' in lang_code else lang_code, None


with open('locales.json') as f:
    _locale = Dotable(json.load(f)[lang]['faker'])
    if sublang:  # TODO check this is actually the way it's done
        _locale.update(Dotable(json.load(f)[lang_code]['faker']))



# Base class all classes inherit from this
class Faker(object):
    pass

def _faker_factory(_loc=None, _where=''):
    if _loc is None:
        _loc = _locale

    if isinstance(_loc, list):
        if all(isinstance(s, basestring) for s in _loc):
            # then method
            # TODO is the all above necessary? Maybe any would do?
            # TODO format string, and #s
            # dict(dir(_where), **locals()) how to get it?
            
            @classmethod
            def choice_(cls):
                return format_(random.choice(_loc))
            return choice_
        else:
            # it's a class
            assert(not any(isinstance(s, basestring) for s in _loc))
            # fingers crossed

            if all(isinstance(s, list) for s in _loc):
                # I'm assuming everything in each list is a string... why wouldn't it be?
                # I'm just going to arbitrarily use space here
                @classmethod
                def choice_(cls):
                    return format_(' '.join(map(random.choice, L) for L in _loc))
                return choice_
            else: 
                assert False


    elif isinstance(_loc, dict):
        klass_names = _loc.keys()
        klasses = {}
        for kname in klass_names:
            if isinstance(_loc[kname], list):
                # then possibly method
                klasses[kname] = _faker_factory(_loc[kname], _where='%s.%s' % (_where, kname))
            else:
                # then dictionary and definitely a class
                klassy_name = to_camel(kname)
                # it jolly well ought to be a dict
                assert(isinstance(_loc[kname], dict))
                ty_dict = dict((k, _faker_factory(_loc=v, _where='%s.%s' % (_where, kname)))
                                for k, v in _loc[kname].items())
                klasses[klassy_name] = type(klassy_name, (Faker,), ty_dict)
        return klasses

Fake = Dotable(_faker_factory(_locale))


# Apparently the below is naughty, and I should be overwriting string.Formatter
#.format(dict(dir(classname), **locals()))