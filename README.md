A python library for generating pseudo-random (but "realistic") data.

### How to install

The easiest way is to install via [pip](http://www.pip-installer.org/en/latest/installing.html):

    pip install pyfaker

### Usage

Works with many languages and locales (the same as [Ruby's Faker](http://faker.rubyforge.org/)) so your fake data will be relevant to your location.

```
In [1]: from pyfaker import Fake

In [2]: fake = Fake(lang_code='en')

In [3]: fake.Address.street_address()
Out[3]: u'72449 Ward Shore'

In [4]: fake.Address.street_address()
Out[4]: u'7954 Waelchi Mall'

In [5]: fake.Company.bs()
Out[5]: u'whiteboard visionary markets'

In [6]: fake.Company.bs()
Out[6]: u'exploit innovative paradigms'

In [7]: fake.Name.name()
Out[7]: u'Aaliyah Bauch'

In [8]: fake.Name.name()
Out[8]: u"Chad O'Keefe"

In [9]: fake_de = Fake('de')

In [10]: fake_de.Address.street_address()
Out[10]: u'Imbacher Weg 471'

In [11]: fake_de.Address.city()
Out[11]: u'Schreiberdorf'

In [12]: fake_gb = Fake('en-gb')

In [13]: fake_gb.PhoneNumber.formats()
Out[13]: u'0800 906569'

In [14]: fake_gb.PhoneNumber.formats()
Out[14]: u'01662 12756'

```
*all of this is generated from the faker gem's yamls.*

The languages, which may have different levels of support:

```
In [14]: from pyfaker import LANGS

In [15]: print LANGS
[u'en-gb', u'fr', u'en-us', u'nl', u'vi', u'de', u'de-ch', u'en-ind', u'en-au', u'en', u'pt-br', u'en-bork', u'en-ca', u'pl', u'no-nb'
```

*Here, `en-gb` denotes British English, etc.*

### Creating random classes

One way is to put the instance of Fake as a default argument to `__init__`, this means that it's only created once (when it's defined):

```
class Person:
    def __init__(self, fake=Fake()):
        self.name = fake.Name.name()
        self.phone_number = fake.PhoneNumber.formats()

p = Person()

# access the attributes
p.name
p.phone_number
```

### Bugs / Features

Please [create a github issue](https://github.com/hayd/pyfaker/issues), if *you* can fix whatever it: pull-requests are much appreciated! :)

####Next up:

- more sentences and other standard random things
- make decorator (?) or apply to classes?
- guess what to fake based on names

[![Build Status](https://travis-ci.org/hayd/pyfaker.png?branch=master)](https://travis-ci.org/hayd/pyfaker)