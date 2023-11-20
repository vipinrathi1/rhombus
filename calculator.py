def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    n1 = float(input("What's the first number: "))
    for symbol in operations:
        print(symbol)
    y = True
    while y:
        operation_symbol = input("Pick an operation from the line above: ")
        n2 = float(input("What's the next number: "))
        result = operations[operation_symbol](n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {result}")
        again = input("Type 'y' if want to continue with {result} or 'n' to start a new calculator: ")
        if not again == "y":
            y = False
        else:
            n1 = result
        if again == "n":
            calculator()

calculator()







