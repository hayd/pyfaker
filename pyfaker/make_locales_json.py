import yaml
import hashlib
import json
import os
import re


langs = ['de-ch', 'en-bork', 'en-ind', 'fr', 'pl', 'de', 'en-ca',
         'en-us', 'nl', 'pt-br', 'en-au', 'en-gb', 'en', 'no-nb', 'vi']

# in future this should scrape them from the ruby faker site without needing to copy them
# we'll want to iterate through them but for now we'll just open en.yml


def unruby(json_):
    if isinstance(json_, basestring):
        # TODO replace all #{foo_bar.baz} with {FooBar.baz}, may not be needed
        return re.sub('#({[^}]*})', r'\1', json_)
    if isinstance(json_, list):
        return map(unruby, json_)
    if isinstance(json_, dict):
        return dict((k, unruby(v)) for k, v in json_.items())
    return json_


def _curpath():
    pth, _ = os.path.split(os.path.abspath(__file__))
    return pth


def get_yaml(lang='en'):
    yml_dict = {}
    fpath = os.path.join(_curpath(), 'locales/%s.yml' % lang)
    with open(fpath, 'r') as f:
        f_yml = yaml.load(f)
        f_yml[lang]['_md5'] = hashlib.md5(f.read()).hexdigest()
        yml_dict.update(f_yml)
    return yml_dict

# TODO iterate over all yamls (and update the dict)


def save_json(langs):
    locales = {}
    for lang in langs:
        loc = unruby(get_yaml(lang))
        locales.update(loc)
    fpath = os.path.join(_curpath(), 'locales.json')
    with open(fpath, 'w') as f:
        json.dump(locales, f)
save_json(langs)
