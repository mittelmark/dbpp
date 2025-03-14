<center>
    __Applications:__ 
    [mkdoc](../mkdoc/mkdoc.md) -
    [krokiencoder](../kroki/krokiencoder.md) -
    [sfa](../sfa/sfa.md) -
    [pydoc2md](../pydoc2md/pydoc2md.md)
</center>
## Convert Python Google docs docstrings into Markdown

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

## Module Functions


## pydoc2md.pydoc2md(infile,outfile="")

Convert docstrings of the given Python file to a Markdown document.

This function converts embedded Google docstrings into Markdown which
can be then converted to HTML for instance using the pandoc document converter.


__Args:__

* infile (str) : Python file with docstrings in Google format
* outfile (str): optional output file, if not given, Markdown code
                   is printed to stdout
    

__Returns:__

* None

## pydoc2md.test(msg)

This is a test method - arguments: msg - message to print

## pydoc2md.main(argv)

The main function of the module,  argv is usually sys.argv.
