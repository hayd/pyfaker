Game plan:

1. Scrape yamls from ruby gem faker (not important)
2. From yamls extract json also removing `#{foo.bar}` ruby syntax with lovely `{Foo.bar()}`
~~3. From json extract classes using metaclasses (whoop!)~~
4. Classes should be imported into module as one would expect.
5. How to use these: as decorators? or an optional `fake` flag?
6. Seed support.
7. Guess how to fake (given variable name, which is it most likely to be)

Next up:
clean up json to use Python format, #{foo.bar} to {Foo.bar}, am I right in thinking all but the last are classes, so it's Foo.Bar.baz)
work out how to make a Formatter to call Foo.bar() "using format"
replace #s with random digit: http://stackoverflow.com/questions/12449555/python-string-replacement-with-random-items