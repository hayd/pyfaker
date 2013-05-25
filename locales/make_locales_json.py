# get locales from ruby

import yaml
import hashlib
import json

lang = 'en'

# in future this should scrape them from the ruby faker site without needing to copy them here
# we'll want to iterate through them but for now we'll just open en.yml


_locales = {}
with open('%s.yml' % lang, 'r') as f:
    f_yml = yaml.load(f)
    f_yml[lang]['_md5'] = hashlib.md5(f.read()).hexdigest()
    _locales.update(f_yml)

with open('locales.json', 'w') as f:
    json.dump(_locales, f)




# locales.en.faker.name => ['first_name', 'last_name', 'suffix', 'title', 'prefix', 'name']


# The keys are the language "short" e.g. 'en'