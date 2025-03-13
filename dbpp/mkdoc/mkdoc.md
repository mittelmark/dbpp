<center>
    [mkdoc](../mkdoc/mkdoc.md) -
    [pydoc2md](../pydoc2md/pydoc2md.md) -
    [krokiencoder](../kroki/krokiencoder.md)
</center>
## Convert Markdown files into HTML

This is a command line application which allows you do convert Markdown files or documentation
for programming code embedded into the source code after a `#'` comment into HTML files.
Further it is possible to convert Github compatible Markdown to Gitlab Markdown by providing an 
output filename with a `.md` extension.

Author: Detlef Groth, University of Potsdam, 2021-2025

License: MIT

Usage as command line application: 

    python3 -m dbpp.mkdoc INFILE OUTFILE ?CSSFILE?

Usage as module:

    import dbpp.mkdoc as mkdoc
    mkdoc.mkdoc.main(MDFILE,HTMLFILE,CSSFILE)
    mkdoc.mkdoc.main(MDFILE,MDFILE)
    
Conversion to a HTMLFILE requires the modules mkdoc pymdown-extensions
to be installed, Links pointing to MD files are converted to links pointing 
to HTML files..

## Module Functions


## mkdoc.extract(infile,outfile)

Extracts the embedded Markdown 

## mkdoc.md2gitlabmd(infile,outfile)

Converts the given inoutfile in Markdown to Gitlab compatible Markdown

## mkdoc.md2html(mdfile,outfile,cssfile)

Converts the given Markdown infile to the given HTML outfile
