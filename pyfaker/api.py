"""This module defines ApiMixin which defines shortcuts to the main Fake
class."""

import random


class ApiMixin(object):

    def full_name(self):
        "Returns a full name, this may have a title or suffix."
        return self.Name.name()

    def first_name(self):
        "Returns a first name for the locale."
        return self.Name.first_name()

    def last_name(self):
        "Returns a last name for the locale."
        return self.Name.last_name()

    def street_address(self):
        "Returns a street address for the locale."
        return self.Address.street_address()

    def secondary_address(self):
        "Returns a secondary address for the locale, e.g. an apartment number."
        return self.Address.secondary_address()

    def city(self):
        "Returns a city in the locale."
        return self.Address.city()

    def state_abbr(self):
        "Returns a state abbreviation e.g. CA."
        return self.Address.state_abbr()

    def postcode(self):
        "Returns a postal code for the locale."
        return self.Address.postcode()

    def phone_number(self):
        "Returns a phone number for the locale."
        return self.PhoneNumber.formats()

    def company_name(self):
        "Returns a company name for the locale."
        return self.Company.name()

    def lorem_sentence(self, n=None):
        "Returns a lorem sentence of length n."
        if n is None:
            n = random.randint(15, 30)
        rest = ' '.join([self.Lorem.words() for _ in range(n - 1)])
        return self.Lorem.words().title() + rest + '.'

    def lorem_paragraph(self, n=None):
        "Returns a lorem paragraph with n sentences."
        if n is None:
            n = random.randint(4, 7)
        return ' '.join([self.lorem_sentence() for _ in range(n)])
