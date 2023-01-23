"""
The dbpp.kroki terminal application.
"""


import dbpp
import dbpp.kroki.KrokiEncoder as KrokiEncoder
import sys, re, os
def usage(argv):
    print("\nUsage: python3 -m dbpp.kroki URL|DIAGRAMFILE")
    print("\nExample:\n\npython -m dbpp.kroki https://kroki.io/plantuml/svg/eNpLzkksLlZwVKhWqAUAF10DsA==")
    print("\nVersion:\t"+dbpp.__version__+"\nAuthor:\t"+dbpp.__author__+"\n")
    print("For reading the manual use: python -m dbpp.kroki --man")
    exit(0)

def main(argv):
    if "-h" in argv or "--help" in argv or len(argv) == 1:
        usage(argv)
    if "-m" in argv or "--man" in argv or len(argv) == 1:
        print(dbpp.kroki.__doc__)
        exit(0)
    kroki=KrokiEncoder.KrokiEncoder()
    if (len(argv) >= 2):
        if re.search("^https://.+(svg|png|pdf)/",argv[1]):
            print(kroki.kroki2dia(argv[1]))
        elif re.search(".+\.[a-z]{3,6}$",argv[1]):
            if os.path.exists(argv[1]):
                dia = "ditaa"
                if re.search("dot$",argv[1]):
                    dia="graphviz"
                elif re.search("pu?ml$",argv[1]):
                    dia="plantuml"
                elif re.search("erd$",argv[1]):
                    dia="erd"
                print(kroki.dia2kroki(argv[1],dia=dia))
            else:
                print(f"Error: File `{argv[1]}` does not exists!")
        else:    
            usage(argv)
            print("Error: wrong arguments!")                

if __name__ == "__main__":
     main(sys.argv)
