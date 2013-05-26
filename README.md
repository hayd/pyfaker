### This is a work in progress.

Currently only the English (from en.yml) is used:

```
In [1]: from pyfaker import Fake

In [2]: fake = Fake(lang_code='en')

In [3]: fake.Address.street_address()
Out[3]: u'72449 Ward Shore'

In [4]: fake.Address.street_address()
Out[4]: u'7954 Waelchi Mall'

In [5]: f.Company.bs()
Out[5]: u'whiteboard visionary markets'

In [6]: f.Company.bs()
Out[6]: u'exploit innovative paradigms'

In [7]: f.Name.name()
Out[7]: u'Aaliyah Bauch'

In [8]: f.Name.name()
Out[8]: u"Chad O'Keefe"
```
*all of this is generated from the yamls.*

####Why:

1. to port to python the (amazing) faker ruby gem and its fantastic language support and bring this to python (and do so in a dynamic way, in the sense that we can get benefit from updates when this is updated just by using their yml files).
2. For me to learn about metaclasses and stuff... I've now recoded in a saner way.

####Game plan:

1. Scrape yamls from ruby gem faker (not important, can just copy for the moment)
2. ~~From yamls extract json also removing `#{foo.bar}` ruby syntax with lovely `{Foo.bar}`~~
3. ~~From json extract classes using metaclasses (whoop!)~~
4. ~~Formatter to string substitute `{Foo.bar}` with `Foo.bar()`~~
5. ~~Import classes when importing the module as one would expect.~~ Just import `Fake` class.
6. Decide how to use these: as decorators? or an optional `fake` flag? Not sure.
7. Use seed with random, I suspect it could be useful and easy.
8. Testing, ~~even just checking the methods are callable is pretty useful~~. Support for python 2.6+ and 3.
9. "Guess how to fake" (given variable name (?), which is it most likely to be)
10. ? 

####Next up:

- add in all the other languages (and cross fingers)
- ...