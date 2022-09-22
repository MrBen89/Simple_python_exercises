import pandas


code_data = pandas.read_csv("nato_phonetic_alphabet.csv")
code_data_frame = pandas.DataFrame(code_data)



code ={}
for (index, row) in code_data.iterrows():
    code[row.letter] = row.code


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

input_word = input("Please enter a word: ").upper()

result = [code[letter] for letter in input_word]

print(result)
