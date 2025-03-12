#!/usr/bin/env python3
"""Convert Python Google docs docstrings into Markdown

This is a command line application which allows you do convert Python docstrings
documentation in Google docstrings format into Markdown documentation which
can be then converted into HTML documentation using document converters such as
pandoc.

Author: Detlef Groth, University of Potsdam, 2024-2025

License: MIT

Usage as command line application: 

    pydoc2md PYTHONFILE ?MDFILE?

Usage as module:

    import pydoc2md
    pydoc2md.pydoc2md PYTHONFILE ?MDFILE?

"""

import sys, os, re, shutil
import argparse

def pydoc2md(infile,outfile=""):
    """Convert docstrings of the given Python file to a Markdown document.
    
    This function converts embedded Google docstrings into Markdown which
    can be then converted to HTML for instance using the pandoc document converter.
    
    Args:
        infile (str) : Python file with docstrings in Google format
        outfile (str): optional output file, if not given, Markdown code
                       is printed to stdout
        
    Returns:
        None
    """
    file = open(infile,'r')
    if (outfile != ""):
        out  = open(outfile,'w')
    else:
        out = sys.stdout
        
    lnr   = 0    # global line number
    mod   = False
    dflnr = 0  # def line number
    func  = False
    funcheader = False
    mtlnr = 0  # method of class line number
    meth  = False
    cllnr = 0  # class line number
    clss  = False
    for line in file:
        line = re.sub("\t","    ",line)
        lnr   = lnr + 1
        dflnr = dflnr + 1 
        cllnr = cllnr + 1
        mtlnr = mtlnr + 1        
        ## handline module documentation
        if lnr == 2 and re.search('^"""', line):
            out.write("## "+re.sub('"""',"",line))
            ## not a single line docstring?
            if not re.search('""".+"""\\s*$',line):        
                mod = True
        elif lnr > 1 and mod and re.search('^"""',line):
            out.write("\n")
            mod = False
        elif mod:
            out.write(line)
            continue
        ## handling functions    
        if re.search("^def",line):
            dfname = re.sub("def +([^ ]+):","\\1",line)
            dflnr = 0
            clss = False
            meth = False
        elif dflnr < 3 and re.search('^ {4}"""',line):
            ## not a single line docstring?
            if not re.search('""".+"""\\s*$',line):        
                func  = True
            if not(funcheader):
                out.write("## Functions\n\n")
                funcheader=True
            out.write("\n## "+dfname+"\n")
            out.write(re.sub('"""','',re.sub("^ +","",re.sub(' {4}""" *',"",line))))
            continue
        elif func and re.search('^    """',line):
            func = False
            continue
        elif func and re.search('^    (Args|Returns):',line):
            m = re.match(r"    (Args|Returns):",line)
            out.write(f'__{m.group(1)}:__\n\n')
            continue
        elif func and re.search("^ {8}[^\\s\n]",line):
            out.write(re.sub("^ {8}","* ",line))
        elif func:
            out.write(re.sub("^ {4}","",line))
        ## handling class doc string
        if re.search("^class",line):
            clname = re.sub("class +(.+):","\\1",line)
            cllnr = 0
        elif cllnr == 1 and re.search('^ {4}"""',line):
            out.write("\n## Class: "+clname+"\n")
            out.write(re.sub('"""',"",re.sub("^ +","",re.sub('   """ *',"",line))))
            ## not a single line docstring?
            if not re.search('""".+"""',line):
                  clss  = True
        elif clss and re.search('^    """',line):
            clss = False
        elif clss:
            out.write(re.sub("^ {4}","",line))
        ## handling class methods
        if re.search("^    def .+self",line):
            if re.search(".+:",line):
                mtname = re.sub("def +(.+):.*","\\1",line)
            else:
                mtname = re.sub("^ +def +(.+)","\\1",line)
            mtname = re.sub("_","\\_",mtname)            
            mtlnr = 0
        elif mtlnr < 3 and re.search('^ {8}[a-zA-Z]',line):
            mt2 = re.sub("^ +","",line)
            mtname=mtname+mt2
            mtname=re.sub("\n","",mtname)
            mtname=re.sub(":\\s*$","",mtname)
        elif mtlnr < 3 and re.search('^ {8}"""',line):
            ## not a single line docstring?
            if not re.search('""".+"""',line):
                meth  = True
            out.write("\n### "+mtname)
            out.write(re.sub('"""','',re.sub("^ +","",re.sub('   +""" *',"",line))))
        elif meth and re.search('^ {8}"""',line):
            meth = False
        elif meth and re.search('^ {8}(Args|Returns):',line):
            m = re.match(r"^ {8}(Args|Returns):",line)
            out.write(f'__{m.group(1)}:__\n\n')
        elif meth and re.search("^ {11,12}[^\\s\\n]",line):
            out.write(re.sub("^ {11,12}","* ",line))
        elif meth:
            out.write(re.sub("^ {8}","",line))
    if (outfile != ""):
        out.close()
    file.close()
### just for testing docstrings
def test(msg):
    """This is a test method - arguments: msg - message to print"""
    print(msg)
    
def main(argv):
    """The main function of the module,  argv is usually sys.argv."""
    parser = argparse.ArgumentParser(
            description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--pyfile","-f",type=str,help="a Python module file")
    parser.add_argument("--outfile","-o",type=str,help="a Markdown output file")     
    args = parser.parse_args(argv[1:])
    if args.pyfile and not(os.path.exists(args.pyfile)):
        print(f"Error: file {args.pyfile} does not exists!")
        sys.exit(0)
    if not(args.pyfile):
        print(f"Error: Argument --pyfile FILENAME missing!")
        sys.exit(0)
    if not(args.outfile):
        pydoc2md(args.pyfile,"")
    else:
        pydoc2md(args.pyfile,args.outfile)
    #   pandoc="pandoc"
    #else:
    #   print("Error: pandoc is not installed or not in your PATH!\Please install pandoc\n")
    
if __name__ == "__main__":
     main(sys.argv)
        
