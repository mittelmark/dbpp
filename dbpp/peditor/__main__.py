#!/usr/bin/env python3
"""
This is the PumlEditor command line application.

You should be able to run this application from the terminal direct if the dbpp package is installed completly using this syntax:

    python -m dbpp.peditor ?DIAGRAMFILE?
    
The filename for a diagram is optional.
"""
import os, sys
import dbpp.peditor.pumleditor as peditor

if __name__ == '__main__':
    peditor.main(sys.argv)
