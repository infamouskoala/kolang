import sys

def BasicEval(expression):
    filename = sys.argv[1]
    file = open(filename,"r")
    expression = file.read()
    x = eval(expression)
    return x

def Integration(input):
    filename = sys.argv[1]
    file = open(filename,"r")
    input = file.read()
    if input == "int()":
        print("Function is empty!")
    elif input == "int(dx)":
        x = "x"
        return x
    else:
        print("Syntax error, Invalid syntax in file", filename)
