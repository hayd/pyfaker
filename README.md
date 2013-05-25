### This is a work in progress.

Currently only the English (from en.yml) is used:

```
In [1]: from pyfaker import Fake

In [2]: fake = Fake(lang_code='en')

In [3]: fake.Address.postcode()
Out[3]: u'74358-7434'

In [4]: fake.Address.postcode()
Out[4]: u'22239-1043'

In [5]: fake.Name.name()  # NotImplemented yet
Out[5]: u'{first_name} {last_name}'
```
*all of this is generated on the fly.*

####Why:

1. to port to python the (amazing) faker ruby gem and its fantastic language support and bring this to python (and do so in a dynamic way, in the sense that we can get benefit from updates when this is updated just by copying and pasting their yml files).
2. For me to learn about metaclasses and stuff...

####Game plan:

1. Scrape yamls from ruby gem faker (not important, can just copy for the moment)
2. ~~From yamls extract json also removing `#{foo.bar}` ruby syntax with lovely `{Foo.bar}`~~
3. ~~From json extract classes using metaclasses (whoop!)~~
4. Formatter to string substitute `{Foo.bar}` with `Foo.bar()`, for now as a workaround use `_call`.
5. ~~Import classes when importing the module as one would expect.~~ Just import `Fake` class.
6. Decide how to use these: as decorators? or an optional `fake` flag? Not sure.
7. Add seed support with random, I suspect it could be useful and easy.
8. Testing, even just checking the methods are callable is pretty useful. Support for python 2.6+ and 3.
9. "Guess how to fake" (given variable name (?), which is it most likely to be)
10. ? 

####Next up:

- check every thing but the last is camelcaps {Foo.bar} {Foo.Bar.baz} are classes.
- **work out how to make a Formatter to call Foo.bar() "using format"**
- ~~dynamic import of classes when defining module? (actually I'm not sure this is needed)~~
- dynamic testing via dir (to cover all methods of every class in every language)
- add in all the other languages (and cross fingers)