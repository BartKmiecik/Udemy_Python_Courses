#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


def append_letter():
    letter = open('Input/Letters/starting_letter.txt')
    i = 0
    temp = ''
    for line in letter.readlines():
        if i == 0:
            pass
        else:
            temp += '\n'
            temp += line.strip()
        i += 1
    letter.close()
    return temp

with open('Input/Names/invited_names.txt') as names:
    for name in names.readlines():
        temp_name = name.strip()
        new_file = open(f'Output/ReadyToSend/{temp_name}.txt', 'w')
        new_file.write('Dear ' + temp_name + append_letter())
        new_file.close()


