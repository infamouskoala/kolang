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
    # integration of 1/x or x inverse
    elif input == "int(1/x)" or input == "x^-1":
        return "log(x)"
    # integration of log x
    elif input == "int(log(x))":
        return "xlogx - x"
    else:
        print("Syntax error, Invalid syntax in file", filename)
