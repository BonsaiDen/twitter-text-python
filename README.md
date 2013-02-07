# twitter-text-python

__twitter-text-python__ is a tweet parser and formatter for Python.

It is based on [twitter-text-java](http://github.com/mzsanford/twitter-text-java) 
and passes all the unittests of [twitter-text-conformance](http://github.com/mzsanford/twitter-text-conformance) 
plus some additional ones.

### Usage

```
    >>> import ttp
    >>> p = ttp.Parser()
    >>> result = p.parse("@BonsaiDen Hey that's a great Tweet parser! #ttp")
    >>> result.reply
    'BonsaiDen'
    >>> result.users
    ['BonsaiDen']
    >>> result.tags
    ['ttp']
    >>> result.urls
    []
    >>> result.html
    u'<a href="http://twitter.com/BonsaiDen">@BonsaiDen</a> Hey that\'s a great Tweet Parser! 
    <a href="http://search.twitter.com/search?q=%23twp">#ttp</a>'
```

If you need different HTML output just subclass and override any of the `format_*` methods.


### Contributing


The source is available at [GitHub](http://github.com/BonsaiDen/twitter-text-python), to
contribute to the project, fork it on their and send a pull request.
Everyone is welcome to make improvements to __ttp__!



## License

*MIT*

Copyright (c) 2012 Ivo Wetzel.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

Copyright (c) 2010-2013 Ivo Wetzel

