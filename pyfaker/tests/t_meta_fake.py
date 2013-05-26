import unittest
from pyfaker.meta_fake import Fake

langs = ['en']
all_fakes = {lang_code: Fake(lang_code=lang_code) for lang_code in langs}

# list of tuples descibing location of all methods
all_methods = [('Lorem', 'supplemental'), ('Lorem', 'words')]
# TODO actually generate all_methods


def get_method(self, fake, where):
    for i in where:
        fake = fake.__dict__[i]

    def method(self):
        return fake
    return method


def tmc_t_name(lang_code, where):
    return 'test_' + lang_code + '_' + '_'.join(where)


def tmc_t(lang_code, where):
    fake = all_fakes[lang_code]

    def _t(self):
        self.method = get_method(self, fake, where)
        self.method()  # we shouldn't raise here
    _t.func_name = tmc_t_name(lang_code, where)
    _t.func_doc = 'Test whether %s can be called (with 0 arguments)' % '.'.join(
        where)
    return _t


tmc_dict = {tmc_t_name(lang_code, where): tmc_t(lang_code, where)
            for lang_code in langs
            for where in all_methods}
print tmc_dict

TestMethodsCallable = type('TestMethodsCallable', (
    unittest.TestCase,), tmc_dict)

# klasses[klassy_name] = type(klassy_name, (BaseFake,), ty_dict)
