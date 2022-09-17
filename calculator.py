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

num1 = int(input("Whats the first number?"))
num2 = int(input("Whats the second number?"))
operation = input("Which operator do you want to use? ( +, -, /, *) ")

#Pull the function with the corresponding operator from the dictionary
answer = operations[operation](num1, num2)

print(f"{num1} {operation} {num2} = {answer}")
