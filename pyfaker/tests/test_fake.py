import unittest
from pyfaker import Fake

# list of tuples descibing location of all methods (have this from
# fake._methods)

langs = ['en', 'en-gb']


class TestFakeCallable(unittest.TestCase):
    def setUp(self):
        self.fake = Fake()

    def test_callable(self):
        for method, func in self.fake._methods.items():
            func()

    def test_at_least(self):
        old_methods = [
            'Address.street_name', 'Address.building_number', 'Name.prefix', 'last_name', 'Company.suffix', 'Name.name', 'Address.street_suffix', 'street_name', 'Company.name', 'Lorem.supplemental', 'Internet.domain_suffix', 'Address.street_address', 'prefix', 'Address.state_abbr', 'postcode', 'Company.buzzwords', 'city_prefix', 'Address.secondary_address', 'Name.suffix', 'suffix', 'city', 'first_name', 'buzzwords', 'free_email', 'Address.city_suffix', 'street_suffix', 'Address.time_zone', 'Name.Title.level',
            'state', 'Name.Title.descriptor', 'domain_suffix', 'PhoneNumber.formats', 'Name.first_name', 'Address.country', 'Lorem.words', 'Address.city', 'secondary_address', 'Address.default_country', 'Name.last_name', 'job', 'default_country', 'state_abbr', 'words', 'bs', 'city_suffix', 'Address.postcode', 'supplemental', 'Internet.free_email', 'name', 'level', 'country', 'time_zone', 'building_number', 'Name.Title.job', 'descriptor', 'Company.bs', 'formats', 'Address.state', 'Address.city_prefix', 'street_address']
        self.assert_(len(old_methods) <= len(self.fake._methods))

'''
for l in langs:
    class Test
    '''
