from src.ext import Ext
from src.interpreter import BasicEval, Integration
import sys

filename = sys.argv[1]
Ext()

file = open(filename,"r")  
reader = file.read()

for i in reader:
    if i in ['+','-','*','**','/','//']:
        print(BasicEval(reader))
    elif i in ["int()"]:
        print(Integration(reader))