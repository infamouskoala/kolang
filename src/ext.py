import sys
def Ext():
    filename = sys.argv[1]  
    if not filename.endswith('.kl'):
        print('Extension error! Koalng uses ".kl" extention only!')
        exit(0)