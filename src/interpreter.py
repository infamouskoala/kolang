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

    # empty function
    if input == "int()":
        return(f"Integration function in file {filename} is empty!")
    # Integration of (dx)
    elif input == "int(dx)":
        return "x"

    else:
        print("Syntax error, Invalid syntax in file", filename)
