import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for index in range (0, len(letters)):
    letters.append(letters[index].upper())

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "£", "%", "$", "&", "/", "(", ")"]

print("Welcome to the pass word generator!")
nr_letters = int(input("How many letters would you like in your password?"))
nr_numbers = int(input("How many numbers would you like in your password?"))
nr_symbols = int(input("How many symbols would you like in your password?"))
pass_length = nr_numbers + nr_letters + nr_symbols

password = ""

for letter in range (0, nr_letters):
        rand = random.randint(0,len(letters)-1)
        password += letters[rand]
for number in range (0, nr_numbers):
        rand = random.randint(0,len(numbers)-1)
        rand_insert = random.randint(0,len(password)-1)
        password = password[:rand_insert] + numbers[rand] + password[rand_insert:]
for symbol in range (0, nr_symbols):
        rand = random.randint(0,len(symbols)-1)
        rand_insert = random.randint(0,len(password)-1)
        password = password[:rand_insert] + symbols[rand] + password[rand_insert:]


print(password)
