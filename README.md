### This is a work in progress.

Currently only the English (from en.yml) is used:

```
In [1]: from pyfaker import Fake

In [2]: Fake.Address.street_address()  # This should be populated with generated stuff
Out[2]: u'{building_number} {street_name}'

In [3]: Fake.Name.first_name()
Out[3]: u'Eunice'
```

*all of which is dynamically generated.*

####Why:

1. to port to python the (amazing) faker ruby gem and its fantastic language support and bring this to python (and do so in a dynamic way, in the sense that we can get benefit from updates when this is updated just by copying and pasting their yml files).
2. For me to learn about metaclasses and stuff...

####Game plan:

1. Scrape yamls from ruby gem faker (not important, can just copy for the moment)
2. ~~From yamls extract json also removing `#{foo.bar}` ruby syntax with lovely `{Foo.bar}`~~
3. ~~From json extract classes using metaclasses (whoop!)~~
4. Formatter to string substitute `{Foo.bar}` with `Foo.bar()`.
5. Import classes when importing the module as one would expect.
6. Decide how to use these: as decorators? or an optional `fake` flag? Not sure.
7. Add seed support with random, I suspect it could be useful and easy.
8. Testing, even just checking the methods are callable is pretty useful. Support for python 2.6+ and 3.
9. "Guess how to fake" (given variable name (?), which is it most likely to be)
10. ? 

####Next up:

- check every thing but the last is camelcaps {Foo.bar} {Foo.Bar.baz} are classes.
- work out how to make a Formatter to call Foo.bar() "using format"
- dynamic import of classes when defining module?
- add in all the other languages (and cross fingers)