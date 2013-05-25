# get locales from ruby

import yaml
import hashlib
import json
from utils import unruby

lang = 'en'

# in future this should scrape them from the ruby faker site without needing to copy them here
# we'll want to iterate through them but for now we'll just open en.yml


_locales = {}
with open('locales/%s.yml' % lang, 'r') as f:
    f_yml = yaml.load(f)
    f_yml[lang]['_md5'] = hashlib.md5(f.read()).hexdigest()
    _locales.update(f_yml)

_locales = unruby(_locales)

with open('locales.json', 'w') as f:
    json.dump(_locales, f)

# The keys are the language lang_code e.g. 'en'
