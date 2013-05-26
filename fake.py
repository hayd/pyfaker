import random
import re
from utils import to_camel, get_locales, BaseFake, call_fmt


all_locales = get_locales()


class Fake(BaseFake):
    def __init__(self, lang_code='en'):
        self._locale = all_locales[lang_code]['faker']
        # TODO update with other methods e.g. en-ca
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
                            print type(m)
                            # print data.items()[0]
                        #    assert False, (m, ('.'.join([Topic, SubTopic, m]))

                    def sub_topics():
                        pass
                    sub_topics.__dict__ = topic_dict
                    sub_topics.__name__ = SubTopic
                    topic_dict[SubTopic] = sub_topics
                else:
                    print type(data)

            def topics():
                pass  # TODO actually use a proper topics class
            topics.__dict__ = topic_dict
            topics.__name__ = Topic
            self.__dict__[Topic] = topics

    def _format(self, s):
        # replace #s with digits
        def callback(matchobj):
            return '%s' % random.randrange(10)
        s = re.sub(r'#', callback, s)
        # replace {Name.foo} etc.
        s = call_fmt.format(s, **dict(self.__dict__, **self._methods))
        return s
