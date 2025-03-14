<center>
    __Applications:__ 
    [mkdoc](../mkdoc/mkdoc.md) -
    [krokiencoder](../kroki/krokiencoder.md) -
    [sfa](../sfa/sfa.md) -
    [pydoc2md](../pydoc2md/pydoc2md.md)
</center>
## dbpp.sfa - building single file applications

## SYNOPSIS

```{.bash}
python -m dbpp.sfa infile1.py infile2.py ... ?-o outfile.py?
```
 
## DESCRIPTION

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

## EXAMPLE

```{.bash}
python3 -m dbpp.sfa infile1.py infile2.py -o appfile.py
chmod 755 appfile.py
cp appfile.py ~/.local/bin/appfile
appfile -h
```

## Module Functions


## sfa.main(argv)


main function of the sfa module


__Args:__

* argv (list): list with several filenames, the ouput file is
                 given after an -o argument

__Returns:__

   None
   

__Example:__


   ```
   dbpp.sfa.main infile1.py infile2.py infile3.py -o app.py
   ```
