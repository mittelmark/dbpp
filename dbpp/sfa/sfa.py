#!/usr/bin/env python3
"""dbpp.sfa - building single file applications

SYNOPSIS

```{.bash}
python -m dbpp.sfa infile1.py infile2.py ... ?-o outfile.py?
```
 
DESCRIPTION

This a command line tool which allows you to build single file applications 
from several Python files if they follow certain conventions used in the course
Introduction to Databases and Practical Programming at the University of Potsdam. 

These conventions are the followings: if the Python files have possible functions
help, usage or/and main they should come after the actual class or function 
definitions, a block to check for the name check of the application must be
at the very end. These definitions are kept for the last file given on the
command line but removed for for all files before.

The tool concatanates in principle all the given files to a single file.
However it removes all import statements from the files import other file
modules giving on the command line. It as well stops concatanating for the
current file, if it is not the last file, if a function like usage, main or
help is seen on the current line. As well only for the last file the
main/name check is kept. 

EXAMPLE

```{.bash}
python3 -m dbpp.sfa infile1.py infile2.py -o appfile.py
chmod 755 appfile.py
cp appfile.py ~/.local/bin/appfile
appfile -h
```
"""

import sys
import os
import re
def usage(argv):
    print("dbpp.sfa - Building single Python file applications")
    print("Author: Detlef Groth, University of Potsdam, 2024-2025")
    print("License: MIT\n-----------------------------------------")
    print("Usage: python3 -m dbpp.sfa PYTHONFILE ... ?-o OUTFILE?")
    
def main(argv):
    """
    main function of the sfa module
    
    Args:
        argv (list): list with several filenames, the ouput file is
                     given after an -o argument
    Returns:
       None
       
    Example:

       ```
       dbpp.sfa.main infile1.py infile2.py infile3.py -o app.py
       ```
    """
    outfile = ""
    if "-o" in argv:
        idx = argv.index("-o")
        if len(argv)>idx:
            outfile=argv[idx+1]
            del argv[idx]
            del argv[idx]
        else:
            print("Error: Missing output filename after -o option!")
            exit(0)
    files = list()
    modules = list()
    if len(argv) == 2:
        print("Error: At least two Python input files are required!")
        exit(0)
    for arg in argv[1:]:
        if not os.path.exists(arg):
            print(f"Error: File {arg} does not exists!")
            exit(0)
        else:
            files.append(arg)
            modules.append(re.sub("\\.[pP][yY]$","",arg))
    if len(modules) == 0:
        print("Error: At least two Python input files are required!")
        exit(0)
    if outfile != "":
        out  = open(outfile,'w')
        out.write("#!/usr/bin/env python3\n")
    else:
        sys.stdout.write("#!/usr/bin/env python3\n")
    for i in range(0,len(modules)):
        file = open(files[i],'r')
        if (outfile != ""):
            out.write(f"# file: {files[i]}\n")
        else:
            sys.stdout.write(f"# file: {files[i]}\n")
        for line in file:
            if re.match(r"#!/",line):
                continue
            if re.match(r"^(from|import)",line):
                ignore = False
                for mod in modules:
                    if re.search(" "+mod,line):
                        ignore = True
                        break
                if ignore:
                    continue
            if modules[i] != modules[-1]:
                if re.match(r"^def\s+(usage|help|main)",line):
                    break
                if re.match(r"^if\s+__name__",line):
                    break
            if re.match(r"^\s*#'",line):
                continue
            if outfile != "":
                out.write(line)        
            else:
                sys.stdout.write(line)
        file.close()
            
    if outfile != "":
        out.close()
