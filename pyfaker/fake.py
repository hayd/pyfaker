import random
import re
from pyfaker.utils import to_camel, get_locales, call_fmt
from pyfaker.xeger import Xeger


all_locales = get_locales()
xeger = Xeger().xeger


class BaseFake(object):
    pass


class BaseFakeTopic(object):
    def __init__(self, name, topic_dict):
        self.__dict__ = topic_dict
        self.__name__ = name


class Fake(BaseFake):
    def __init__(self, lang_code='en'):
        main_lang = lang_code.split('-')[0]
        if main_lang in all_locales:
            self._locale = all_locales[main_lang]['faker'].copy()
            # update with other locale e.g. en-ca
            # TODO this may have to be a recursive update (don't overwrite
            # nested)
            self._locale.update(all_locales[lang_code]['faker'])
        else:
            try:
                self._locale = all_locales[lang_code]['faker']
            except (KeyError,):
                raise KeyError(
                    "lang-code '%s' is either not supported or not recognised.")

        self._methods = {}
        for topic, methods in self._locale.items():
            Topic = to_camel(topic)
            topic_dict = {}
            for method, data in methods.items():
                if isinstance(data, list):
                    # This bit is a little hacky
                    if method == 'bs' or method == 'buzzwords':
                        def choice(self=self, data=data):
                            words = map(random.choice, data)
                            return self._format(' '.join(words))
                    else:
                        def choice(self=self, data=data):
                            return self._format(random.choice(data))
                    topic_dict[method] = choice
                    self._methods.update([(method, choice), (
                        '.'.join([Topic, method]), choice)])
                elif isinstance(data, dict):
                    # TODO refactor
                    sub_topic = method
                    SubTopic = to_camel(sub_topic)
                    sub_topic_dict = {}
                    for m, d in data.items():
                        if isinstance(d, list):
                            def choice(self=self, d=d):
                                return self._format(random.choice(d))
                            sub_topic_dict[m] = choice
                            self._methods.update([(m, choice), (
                                '.'.join([Topic, SubTopic, m]), choice)])
                        else:
                            raise NotImplementedError
                    sub_topics = BaseFakeTopic(
                        name=SubTopic, topic_dict=sub_topic_dict)
                    topic_dict[SubTopic] = sub_topics
                else:
                    # This bit is a little hacky
                    if method == 'postcode':  # then it's a regex
                        def choice(self=self, data=data):
                            return xeger(data[1:-1])
                        topic_dict[method] = choice
                        self._methods.update([(method, choice), (
                                              '.'.join([Topic, method]), choice)])
                    else:
                        raise NotImplementedError

            topics = BaseFakeTopic(name=Topic, topic_dict=topic_dict)
            self.__dict__[Topic] = topics

    def _format(self, s):
        # replace #s with digits
        def callback(matchobj):
            return '%s' % random.randrange(10)
        s = re.sub(r'#', callback, s)
        # replace {Name.foo} etc.
        s = call_fmt.format(s, **dict(self.__dict__, **self._methods))
        return s
