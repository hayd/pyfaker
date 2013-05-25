import yaml
import hashlib
import json
import os
from utils import unruby

lang = 'en'

# in future this should scrape them from the ruby faker site without needing to copy them
# we'll want to iterate through them but for now we'll just open en.yml


def _curpath():
    pth, _ = os.path.split(os.path.abspath(__file__))
    return pth

def get_yaml(lang='en'):
	yml_dict = {}
	fpath = os.path.join(_curpath(), 'locales/%s.yml' % lang)
	with open('locales/%s.yml' % lang, 'r') as f:
	    f_yml = yaml.load(f)
	    f_yml[lang]['_md5'] = hashlib.md5(f.read()).hexdigest()
	    yml_dict.update(f_yml)
	return yml_dict

# TODO iterate over all yamls (and update the dict)

_locales = unruby(get_yml('en'))

fpath = os.path.join(curpath(), 'locales.json')
with open('locales.json', 'w') as f:
    json.dump(_locales, f)