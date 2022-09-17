def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
answer = 0
will_continue = "y"

while will_continue == "y":
    if answer == 0:
        num1 = int(input("Whats the first number?"))
    else:
        num1 = answer
    operation = input("Which operator do you want to use? ( +, -, /, *) ")
    num2 = int(input("Whats the second number?"))


    #Pull the function with the corresponding operator from the dictionary
    answer = operations[operation](num1, num2)

    print(f"{num1} {operation} {num2} = {answer}")

    will_continue = input("Type 'y' to continue calculating with the previous result, type 'c' to clear, or type 'n' to exit.")
    if will_continue == "c":
        answer = 0
        will_continue = "y"
