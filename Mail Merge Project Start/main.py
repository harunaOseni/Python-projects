#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#merge mail program 

with open(r"C:\Users\oseni haruna\OneDrive\Documents\Python Programming\Day24\Mail Merge Project Start\Input\Names\invited_names.txt")as names: 
    names_list = names.readlines()

    for name in names_list:
        with open(r"C:\Users\oseni haruna\OneDrive\Documents\Python Programming\Day24\Mail Merge Project Start\Input\Letters\Starting_Letter.txt")as starting_letter:
            starting_letter_list = starting_letter.readlines()
            starting_letter_list[0] = starting_letter_list[0].replace("[name]", name.strip("\n")) 
            with open(r"C:\Users\oseni haruna\OneDrive\Documents\Python Programming\Day24\Mail Merge Project Start\Output\ReadyToSend\{}.txt".format(name.strip("\n")), "w") as new_letter:
                for line in starting_letter_list:
                    new_letter.write(line) 

