import caeser_art

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

print(caeser_art.logo)
def start():
    direction = input("Type 'encode' to encrypt, or 'decode' to decrypt.")
    text = input("Type your message: ").upper()
    shift = int(input("Type the shift number: "))%26
    caeser(text, shift, direction)

def caeser(text, shift, direction):
    message = ""
    for letter in text:
        if letter in letters:
            ind = letters.index(letter)
            if direction == "encode":
                message += letters[ind+ shift]
            elif direction == "decode":
                message += letters[ind- shift]
        else:
             message += letter
    print(f"The new message is: {message}.")
    again = input("Do you want to go again? ").lower()
    if again == "yes":
        start()

start()
