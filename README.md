This is a work in progress.

Objectives 

1. to port the (amazing) faker ruby gem and all of it's language support and bring this to python.
2. For me to learn some metaclasses and stuff...

Game plan:

1. Scrape yamls from ruby gem faker (not important)
~~2. From yamls extract json also removing `#{foo.bar}` ruby syntax with lovely `{Foo.bar()}`~~
~~3. From json extract classes using metaclasses (whoop!)~~
4. Format {Foo.bar} with Foo.bar()
5. Import classes when importing the module as one would expect.
6. How to use these: as decorators? or an optional `fake` flag? Not sure.
7. Add seed support to random, I suspect it could be useful.
8. "Guess how to fake" (given variable name, which is it most likely to be)

Next up:
check every thing but the last is camelcaps {Foo.bar} {Foo.Bar.baz} are classes.
work out how to make a Formatter to call Foo.bar() "using format"
dynamic import of classes when defining module?
add in all the other languages (and cross fingers)