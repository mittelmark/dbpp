#!/usr/bin/env python3
"""Convert Python Google docs docstrings into Markdown

This is a command line application which allows you do convert Python docstrings
documentation in Google docstrings format into Markdown documentation which
can be then converted into HTML documentation using document converters such as
pandoc.

Author: Detlef Groth, University of Potsdam, 2024-2025

License: MIT

Usage as command line application: 

    python3 -m dbpp.pydoc2md --pyfile PYTHONFILE \
        ?--outfile MDFILE|HTMLFILE? ?--cssfile CSSFILE?

Usage as module:

    import dbpp.pydoc2md as pydoc2md
    import dbpp.mkdoc as mkdoc
    pydoc2md.pydoc2md(PYTHONFILE,MDFILE)
    mkdoc.mkdoc.main(MDFILE,HTMLFILE,CSSFILE)
    

Direct conversion to a HTMLFILE requires the modules mkdoc pymdown-extensions
to be installed.
"""

import sys, os, re, shutil
import base64
import zlib
import argparse
import dbpp.mkdoc.mkdoc as mkdoc
try:
    import markdown
    md = markdown.Markdown(extensions=['pymdownx.superfences'])
    mkd=True
except:
    mkd = False

def Line_to_dict(line):
    # Remove the leading "```
    line=re.sub(" +",",",line)
    line=re.sub("kroki","",line)
    line=re.sub("[^a-zA-Z0-9_,=]","",line)
    line=re.sub("^,+","",line)
    d = dict()
    for item in line.split(","):
        l = item.split("=")
        key=l[0]
        val=l[1]
        if val.lower() == "true":
            d[key]=True
        elif val.lower() == "false":
            d[key]=False
        else:
            d[key]=val
    return(d)

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
    headerfile=os.path.join(os.path.dirname(infile),"header.md")
    footerfile=os.path.join(os.path.dirname(infile),"footer.md")    
    modname=os.path.splitext(os.path.basename(infile))[0]
    
    header=""
    footer=""
    if os.path.isfile(headerfile):
        file = open(headerfile,'r')
        header=''.join(file.readlines())
        file.close()
            
    if os.path.isfile(footerfile):
        file = open(footerfile,'r')
        footer=file.readLines()
        file.close()
    file = open(infile,'r')
    if (outfile != ""):
        out  = open(outfile,'w')
    else:
        out = sys.stdout
        
    lnr   = 0    # global line number
    mod   = False
    eof   = False
    eofdoc = False
    dflnr = 0  # def line number
    func  = False
    funcheader = False
    kroki = False
    mtlnr = 0  # method of class line number
    meth  = False
    cllnr = 0  # class line number
    clss  = False
    kdict = {'eval': True,'echo':False,'dia': 'ditaa', 'ext': 'png'}
    for line in file:
        line = re.sub("\t","    ",line)
        lnr   = lnr + 1
        dflnr = dflnr + 1 
        cllnr = cllnr + 1
        mtlnr = mtlnr + 1        
        ## handle module documentation
        if lnr == 2 and re.search('^"""', line):
            if header != "":
                out.write(''.join(header))
            out.write("## "+re.sub('"""',"",line))
            ## not a single line docstring?
            if not re.search('""".+"""\\s*$',line):        
                mod = True
        elif lnr > 1 and mod and re.search('^"""',line):
            out.write("\n")
            mod = False
        elif re.search("^ *```.?.kroki",line):
            krokitext=""
            ddef = kdict
            d = Line_to_dict(line)
            for k in d.keys():
                ddef[k] = d[k]
            if ddef["eval"]:
                kroki = True
        elif kroki and re.search("^ *```",line):
            url = base64.urlsafe_b64encode(
            zlib.compress(krokitext.encode('utf-8'), 9)).decode('ascii')
            if ddef['echo']:
                out.write(f"```\n{krokitext}\n```\n")
            out.write(f"![](https://kroki.io/{ddef['dia']}/{ddef['ext']}/{url})\n")
            krokitext=""
            kroki=False
            continue
        elif kroki:
            krokitext=krokitext+line
        elif mod:
            if re.search("^(NAME|SYNOPSIS|DESCRIPTION|EXAMPLE).*",line):
                out.write(f"## {line}")
            else:
                out.write(line)
            continue
        ## handling functions    
        if re.search("^if __name__",line):
            eof = True
        elif eof and re.search("^\"{3}",line):
            eofdoc = True
        elif eofdoc and re.search("^\"{3}",line):
            eofdoc = False
        elif not kroki and eofdoc:
            out.write(line)
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
                out.write("## Module Functions\n\n")
                funcheader=True
            out.write(f"\n## {modname}.{dfname}\n")
            out.write(re.sub('"""','',re.sub("^ +","",re.sub(' {4}""" *',"",line))))
            continue
        elif func and re.search('^    """',line):
            func = False
            continue
        elif func and re.search('^    (Args|Returns|Example):',line):
            m = re.match(r"    (Args|Returns|Example):",line)
            out.write(f'\n__{m.group(1)}:__\n\n')
            continue
        elif func and re.search("^ {8}[^\\s\n]",line):
            out.write(re.sub("^ {8}","* ",line))
        elif not kroki and func:
            out.write(re.sub("^ {4}","",line))
        ## handling class doc string
        if re.search("^class",line):
            clname = re.sub("class +(.+):","\\1",line)
            cllnr = 0
        elif cllnr == 1 and re.search('^ {4}"""',line):
            out.write(f"\n## Class: {modname}.{clname}")
            clname=clname.strip()
            out.write(re.sub('"""',"",re.sub("^ +","",re.sub('   """ *',"",line))))
            ## not a single line docstring?
            if not re.search('""".+"""',line):
                  clss  = True
        elif clss and re.search('^    """',line):
            clss = False
            out.write("\n\n## Methods\n\n")
        elif not kroki and clss:
            out.write(re.sub("^ {4}","",line))
        ## handling class methods
        if re.search("^    def .+self",line):
            if re.search(".+:",line):
                mtname = re.sub(".+def +(.+):.*","\\1",line)
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
            out.write(f"\n### {modname}.{clname}.{mtname}")
            out.write(re.sub('"""','',re.sub("^ +","",re.sub('   +""" *',"",line))))
        elif meth and re.search('^ {8}"""',line):
            meth = False
        elif meth and re.search('^ {8}(Args|Returns):',line):
            m = re.match(r"^ {8}(Args|Returns):",line)
            out.write(f'\n__{m.group(1)}:__\n\n')
        elif meth and re.search("^ {11,12}[^\\s\\n]",line):
            out.write(re.sub("^ {11,12}","* ",line))
        elif not kroki and meth:
            out.write(re.sub("^ {8}","",line))
            
    if footer != "":
        out.write(footer)
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
    parser.add_argument("--pyfile","-f",type=str,help="Python module file")
    parser.add_argument("--outfile","-o",type=str,help="Markdown or HTML output file")     
    parser.add_argument("--cssfile","-c",type=str,help="CSS style file if converted to HTML")         
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
        if args.outfile.endswith(".html"):
            if not(mkd):
                print("Markdown library missing!\nYou must install the Python3 libraries\n Markdown and the extensions like so:\n")
                print("pip3 install pymdown-extensions --user\n")
            else:
                mdfile=re.sub(".py$",".md",args.pyfile)
                pydoc2md(args.pyfile,mdfile)
                if not(args.cssfile):
                    nargs = [argv[0],mdfile,args.outfile]
                else:
                    nargs=[argv[0],mdfile,args.outfile,args.cssfile]
                mkdoc.main(nargs)
        else:                
            pydoc2md(args.pyfile,args.outfile)
    
if __name__ == "__main__":
     main(sys.argv)
        
