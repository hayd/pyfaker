import random
import re
from pyfaker.utils import to_camel, get_locales, BaseFake, call_fmt
from pyfaker.xeger import Xeger


all_locales = get_locales()
xeger = Xeger().xeger

class Fake(BaseFake):
    def __init__(self, lang_code='en'):
        #main_lang = lang_code.split('-')[0]
        self._locale = all_locales[lang_code]['faker']
        # TODO update with other locale e.g. en-ca
        #self._locale = update_loc(self._locale, all_locales[main_lang]['faker'])

        self._methods = {}
        for topic, methods in self._locale.items():
            Topic = to_camel(topic)
            topic_dict = {}
            for method, data in methods.items():
                if isinstance(data, list):
                    # This bit is a little hacky
                    if method == 'bs' or method == 'buzzwords':
                        def choice(data=data, self=self):
                            words = map(random.choice, data)
                            return self._format(' '.join(words))
                    else:
                        def choice(data=data, self=self):
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
                            def choice(d=d, self=self):
                                return self._format(random.choice(d))
                            sub_topic_dict[m] = choice
                            self._methods.update([(m, choice), (
                                '.'.join([Topic, SubTopic, m]), choice)])
                        else:
                            raise NotImplementedError
                    def sub_topics():
                        pass
                    sub_topics.__dict__ = topic_dict
                    sub_topics.__name__ = SubTopic
                    topic_dict[SubTopic] = sub_topics
                else:
                    # This bit is a little hacky
                    if method == 'postcode': # then it's a regex
                        def choice(self=self, data=data):
                            return xeger(data[1:-1])
                        topic_dict[method] = choice
                        self._methods.update([(method, choice), (
                        '.'.join([Topic, method]), choice)])
                    else:
                        raise NotImplementedError

            def topics():
                pass  # TODO actually use a proper topics class
            topics.__dict__ = topic_dict
            topics.__name__ = Topic
            self.__dict__[Topic] = topics

            # Hopefully can do this a the top
            # update with more locale e.g. gb-ca
            # self._sub_locale = all_locales[lang_code]['faker']

    def _format(self, s):
        # replace #s with digits
        def callback(matchobj):
            return '%s' % random.randrange(10)
        s = re.sub(r'#', callback, s)
        # replace {Name.foo} etc.
        s = call_fmt.format(s, **dict(self.__dict__, **self._methods))
        return s
