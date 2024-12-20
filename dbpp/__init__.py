"""
The dbpp package.

This is the "dbpp" package which contains code from the course
Databases and Practical Programming at the University of Potsdam
given since 2018 The following examples can be checked with:
`python -m doctest -v minipy.py`.


Example:
    >>> x = 1
    >>> x + 1
    2
"""

#__path__ = __import__('pkgutil').extend_path(__path__, __name__)

#print(__path__)
from . import kroki
from . import widgets
from . import peditor

__version__ = "0.2.1"
__author__  = "Detlef Groth, University of Potsdam"
__license__ = "MIT"
