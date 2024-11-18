"""
The dbpp.mkdoc terminal application.

"""
import sys
import dbpp.mkdoc as mkdoc
VERSION="0.3.0"    # 2024
def main(argv):
    cssfile=""
    if len(argv)== 4:
        if not(argv[3].endswith(".css")):
            print("Error: Last filename must be a CSS file and have extension .css")
            exit()
        elif not(os.path.exists(argv[3])):
            print(f"Error: Last stylesheet file '{argv[3]}' does not exists!")
            exit()
            
        else:
            cssfile=argv[3]
            argv=argv[0:-1]
    if len(argv)== 3:
        if not(argv[1].endswith(".md")) and argv[2].endswith('.md'):
            extract(argv[1],argv[2]) 
        elif argv[1].endswith(".md") and   argv[2].endswith(".md"):
            print("conversion of two markdown files")
            md2gitlabmd(argv[1], argv[2]) 
        elif argv[2].endswith('.html'):
            if not(mkd):
                print("Markdown library missing!\nYou must install the Python3 libraries\n Markdown and the extensions like so:\n")
                print("pip3 install pymdown-extensions --user\n")
            else:
                if not(argv[1].endswith(".md")):
                    extract(argv[1],'temp.md')
                    mdfile="temp.md"
                else:
                    mdfile=argv[1]
                with open(mdfile, "r", encoding="utf-8") as input_file:
                    text = input_file.read()
                html = md.convert(text)
                head=re.sub("__TITLE__",os.path.basename(argv[1]),head)
                if (cssfile != ""):
                    head=re.sub("__STYLE__",f"<link rel=\"stylesheet\" href=\"{cssfile}\">",head)
                elif  (os.path.exists("style.css")):
                    head=re.sub("__STYLE__","<link rel=\"stylesheet\" href=\"style.css\">",head)
                else:
                    head=re.sub("__STYLE__","",head)
                with open(argv[2], "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
                    output_file.write(head+html+foot)
    else:
        print("mkdoc.py %s - Markdown documentation tool\n\nExtract or convert Markdown code after a `#'` character sequence.\n" % VERSION)
        print("Usage: mkdoc.py infile outfile [cssfile]")
        print("       infile: source code file")
        print("       outfile: Markdown (.md) or HTML (.html) output file")
        print("\nThe Markdown outfile can be processed to html for instance using the syntax:")
        print("       pandoc -i outfile.md -o outfile.html -s --css pandoc.css")
        print("\nAlternatively you can convert directly to HTML like so:")
        print("       mkdoc.py infile.md outfile.html")
        print("\nTo enable direct HTML conversion you need to install the Python package\npymdown-extensions like so:")
        print("       pip3 install pymdown-extensions --user")
        print("\nTo change the look and feel of the output HTML file,\nyou can place a file style.css in the current directory!")
        print("\nCopyright: @ Detlef Groth, University of Potsdam, 2019-2021")
        print("License:   MIT\n")

main(sys.argv)        
