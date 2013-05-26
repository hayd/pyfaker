import random
import re
from utils import to_camel, format_, all_locales, BaseFake


def _faker_factory(_loc=None, _where=''):
    if _loc is None:
        _loc = _locale

    if isinstance(_loc, list):
        if all(isinstance(s, basestring) for s in _loc):
            # then method
            # TODO is the all above necessary? Maybe any would do?

            # dict(dir(_where), **locals()) how to get it?
            @classmethod
            def choice_(cls):
                return format_(random.choice(_loc), current=cls)
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
                    return format_(' '.join(map(random.choice, L) for L in _loc), current=cls)
                return choice_
            else:  # pragma: no cover
                assert False  # let's hope not

    elif isinstance(_loc, dict):
        klass_names = _loc.keys()
        klasses = {}
        for kname in klass_names:
            if isinstance(_loc[kname], list):
                # then possibly method
                klasses[kname] = _faker_factory(_loc[
                                                kname], _where='%s.%s' % (_where, kname))
            else:
                # then dictionary and definitely a class
                klassy_name = to_camel(kname)
                # it jolly well ought to be a dict
                assert(isinstance(_loc[kname], dict))
                ty_dict = dict((k, _faker_factory(_loc=v, _where='%s.%s' % (_where, kname)))
                               for k, v in _loc[kname].items())
                klasses[klassy_name] = type(klassy_name, (BaseFake,), ty_dict)
        return klasses


def _init_fake(self, lang_code='en'):
    lang, sublang = lang_code.split() if '-' in lang_code else lang_code, None
    _locale = _all_locales[lang]['faker']
    if sublang:  # TODO check this is actually the way it's done
        _locale.update(json.load(f)[lang_code]['faker'])
    self.__dict__.update(_faker_factory(_locale))
Fake = type('Fake', (BaseFake,), {'__init__': _init_fake})


# Apparently the below is naughty, and I should be overwriting string.Formatter
#.format(dict(dir(classname), **locals()))
