#!/usr/bin/env python3
"""Command line applications for dbpp.utils."""

import sys
from . import SqlUtils
import sys, os, re

if __name__ == "__main__":
    argv=sys.argv
    if (argv[1] == "sql"):
        del(argv[1])
        SqlUtils.main(argv)
        
