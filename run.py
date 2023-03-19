from src.ext import Ext
from src.interpreter import BasicEval, Integration
import sys

filename = sys.argv[1]
Ext()

file = open(filename,"r")  
reader = file.read()
word = reader.split()

# basic eval
for i in reader:
    if i[0] in ["1","2","3","4","5","6","7","8","9","0"]:
        print(BasicEval(reader))

# Integration
    elif i[0] == "I" or i[0] == "i":
        print(Integration(reader))

# Matrix
    elif i[0] == "M" or i[0] == "m":
        print("")
