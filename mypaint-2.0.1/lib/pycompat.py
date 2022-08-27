# This file is part of MyPaint.
# Copyright (C) 2018 by the MyPaint Development Team
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

"""Convenient consts for use while porting problem Python code.

Trying to avoid six here; the versions we're porting between have the
str/bytes b"" and unicode/str u"" literals, and that seems to be half
the battle for a lot of this stuff.

"""

import sys

PY3 = (sys.version_info >= (3,))
PY2 = (sys.version_info < (3,))

if PY3:
    xrange = range
    unicode = str
else:
    xrange = xrange
    unicode = unicode


# This function is lifed from six.py.
# Copyright (c) 2010-2017 Benjamin Peterson.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions;
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

def add_metaclass(metaclass):
    """Class decorator for creating a class with a metaclass."""
    def wrapper(cls):
        orig_vars = cls.__dict__.copy()
        slots = orig_vars.get('__slots__')
        if slots is not None:
            if isinstance(slots, str):
                slots = [slots]
            for slots_var in slots:
                orig_vars.pop(slots_var)
        orig_vars.pop('__dict__', None)
        orig_vars.pop('__weakref__', None)
        return metaclass(cls.__name__, cls.__bases__, orig_vars)
    return wrapper


# Convenience wrappers for iteritems->items, itervalues->values transition

def iteritems(container):
    """Returns the iterate method of the given container"""
    if PY3:
        return container.items()
    else:
        return container.iteritems()


def itervalues(container):
    """Returns the value iteration method of the given container"""
    if PY3:
        return container.values()
    else:
        return container.itervalues()
