#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as exletter:
    letter = exletter.read()

    new_letter = letter.replace("[name]", "Ben")
    print(new_letter)


with open("./Input/Names/invited_names.txt") as namestxt:
    names = namestxt.readlines()
    for name in names:
        stripped_name = name.strip("\n")
        print(name.strip("\n"))
        new_letter = letter.replace("[name]", stripped_name)
        print(new_letter)
        with open(f"./Output/ReadyToSend/{stripped_name}.txt", mode="w") as file:
            file.write(new_letter)
