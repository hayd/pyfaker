import json
import random
from utils import Dotable


lang_code = 'en'
lang, sublang = lang_code.split() if '-' in lang_code else lang_code, None


with open('locales/locales.json') as f:
    _locale = Dotable(json.load(f)[lang]['faker'])
    if sublang:  # TODO check this is actually the way it's done
        _locale.update(Dotable(json.load(f)[lang_code]['faker']))



# Base class all classes inherit from this
class Faker(object):
    pass

def _faker_factory(_loc=None):
    if _loc is None:
        _loc = _locale

    if isinstance(_loc, list):
        if all(isinstance(s, basestring) for s in _loc):
            # then method
            # TODO is the all above necessary? Maybe any would do?
            # TODO format string
            return lambda self: random.choice(_loc)
        else:
            # it's a class
            assert(not any(isinstance(s, basestring) for s in _loc))
            # fingers crossed

            if all(isinstance(s, list) for s in _loc):
                # I'm just going to arbitrarily use space here
                return lambda self: ' '.join(map(random.choice, L) for L in _loc)
            else: 
                assert False


    elif isinstance(_loc, dict):
        klass_names = _loc.keys()
        klasses = {}
        for kname in klass_names:
            if isinstance(_loc[kname], list):
                # then possibly method
                klasses[kname] = _faker_factory(_loc[kname])
            else:
                # then dictionary and definitely a class
                print kname
                try:
                    klassy_name = kname.title().replace('_', '').encode('ascii')
                except:
                    raise ValueError("%s doesn't convert to a good string for a class name" % kname)
                # it jolly well ought to be a dict
                assert(isinstance(_loc[kname], dict))
                ty_dict = dict((k, _faker_factory(_loc=v))
                                for k, v in _loc[kname].items())
                #d = dict(random_choice, **sub_classes)
                # Note: set(_locale[name].keys()) != set(methods.keys())): this would save some effort if never raises
                klasses[klassy_name] = type(klassy_name, (Faker,), ty_dict)
        return klasses

a = _faker_factory(_locale)


# Apparently the below is naughty, and I should be overwriting string.Formatter
#.format(dict(dir(classname), **locals()))