"""
Command-line application example for dbpp package.
"""
import dbpp
import dbpp.kroki.KrokiEncoder as KrokiEncoder
import sys, re
def usage(argv):
    print("Usage: python3 -m dbpp kroki URL")
def main(argv):
    #print("This is a test run!\n")
    if (len(argv) == 3 and argv[1] == "kroki"):
        #print("here")
        if re.search("^https://.+(svg|png)/",argv[2]):
            kroki=KrokiEncoder.KrokiEncoder()
            print(kroki.kroki2dia(argv[2]))
    #print(argv)

if __name__ == "__main__":
    if "-h" in sys.argv or "--help" in sys.argv:
        usage(sys.argv)
        print("\nExample:\n\npython -m dbpp kroki https://kroki.io/plantuml/svg/eNpLzkksLlZwVKhWqAUAF10DsA==")
        print("\nVersion:\t"+dbpp.__version__+"\nAuthor:\t"+dbpp.__author__+"\n")
    else:
        main(sys.argv)
