code = {
    "A": "▄ ▄▄",
    "B": "▄▄ ▄ ▄ ▄",
    "C": "▄▄ ▄ ▄▄ ▄",
    "D": "▄▄ ▄ ▄",
    "E": "▄",
    "F": "▄ ▄ ▄▄ ▄",
    "G": "▄▄ ▄▄ ▄",
    "H": "▄ ▄ ▄ ▄",
    "I": "▄ ▄",
    "J": "▄ ▄▄ ▄▄ ▄▄",
    "K": "▄▄ ▄ ▄▄",
    "L": "▄ ▄▄ ▄ ▄",
    "M": "▄▄ ▄▄",
    "N": "▄▄ ▄",
    "O": "▄▄ ▄▄ ▄▄",
    "P": "▄ ▄▄ ▄▄ ▄",
    "Q": "▄▄ ▄▄ ▄ ▄▄",
    "R": "▄ ▄▄ ▄",
    "S": "▄ ▄ ▄",
    "T": "▄▄",
    "U": "▄ ▄ ▄▄",
    "V": "▄ ▄ ▄ ▄▄",
    "W": "▄ ▄▄ ▄▄",
    "X": "▄▄ ▄ ▄ ▄▄",
    "Y": "▄▄ ▄ ▄▄ ▄▄",
    "Z": "▄▄ ▄▄ ▄ ▄"
}

text_to_convert = input("Enter text to convert:").upper()
converted_text = text_to_convert

for letter in code:

    converted_text = converted_text.replace(letter, f"{code[letter]}  ")

print(converted_text)
