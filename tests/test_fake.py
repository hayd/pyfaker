import unittest
from pyfaker import Fake

# list of tuples descibing location of all methods (have this from
# fake._methods)

langs = ['de-ch', 'en-bork', 'en-ind', 'pl', 'de', 'en-ca', 'fr',
         'en-us', 'nl', 'pt-br', 'en-au', 'en-gb', 'en', 'no-nb', 'vi']


class TestFake(unittest.TestCase):

    def setUp(self):
        self.fake = Fake()

    def test_has_at_least(self):
        old_methods = [
            'Address.street_name', 'Address.building_number', 'Name.prefix', 'last_name', 'Company.suffix', 'Name.name', 'Address.street_suffix', 'street_name', 'Company.name', 'Lorem.supplemental', 'Internet.domain_suffix', 'Address.street_address', 'prefix', 'Address.state_abbr', 'postcode', 'Company.buzzwords', 'city_prefix', 'Address.secondary_address', 'Name.suffix', 'suffix', 'city', 'first_name', 'buzzwords', 'free_email', 'Address.city_suffix', 'street_suffix', 'Address.time_zone', 'Name.Title.level',
            'state', 'Name.Title.descriptor', 'domain_suffix', 'PhoneNumber.formats', 'Name.first_name', 'Address.country', 'Lorem.words', 'Address.city', 'secondary_address', 'Address.default_country', 'Name.last_name', 'job', 'default_country', 'state_abbr', 'words', 'bs', 'city_suffix', 'Address.postcode', 'supplemental', 'Internet.free_email', 'name', 'level', 'country', 'time_zone', 'building_number', 'Name.Title.job', 'descriptor', 'Company.bs', 'formats', 'Address.state', 'Address.city_prefix', 'street_address']
        self.assert_(len(old_methods) <= len(self.fake._methods))


all_fakes = {}
rng = range(100)
for lang_code in langs:
    all_fakes[lang_code] = Fake(lang_code)

kls_dict = {}
for lang_code in langs:
    for method, func in all_fakes[lang_code]._methods.items():
        if '.' in method:
            method = method.replace('.', '_')

            def test_callable(self=None, func=func):
                for i in rng:
                    func()
            test_name = 'test_%s_%s' % (lang_code.replace('-', '_'), method)
            test_callable.__name__ = str(test_name)
            kls_dict[test_name] = test_callable
        if lang_code == 'vi' and method == 'lorem_words':
            BOO = test_callable


Test_Fake_Methods_Callable = type(
    'Test_Fake_Methods_Callable', (unittest.TestCase,), kls_dict)
