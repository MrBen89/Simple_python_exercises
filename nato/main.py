import pandas

code_data = pandas.read_csv("nato_phonetic_alphabet.csv")
code_data_frame = pandas.DataFrame(code_data)

code ={}
for (index, row) in code_data.iterrows():
    code[row.letter] = row.code

def decode():
    input_word = input("Please enter a word: ").upper()
    try:
        result = [code[letter] for letter in input_word]
        except KeyError:
        print("Sorry, only letters please.")
        decode()
    else:
        print(result)

decode()
