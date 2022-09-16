letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

direction = input("Type 'encode' to encrypt, or 'decode' to decrypt.")

text = input("Type your message: ").upper()
shift = int(input("Type the shift number: "))


def encrypt(input, shift):
    message = ""
    for letter in text:
        ind = letters.index(letter)
        message += letters[ind+ shift]
    print(f"The encoded message is: {message}.")

def decrypt(input, shift):
    message = ""
    for letter in text:
        ind = letters.index(letter)
        message += letters[ind- shift]
    print(f"The encoded message is: {message}.")

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
