# check the later vowel or consonent

while True: # infinite loop
    Latter = input("Enter the latter: ").lower() # take input from user and convert it to lower case
    if Latter in 'aeiou': # check if the latter is in the vowel list
        print(f"{Latter} is a vowel") # print if the latter is a vowel
    elif Latter in 'bcdfghjklmnpqrstvwxyz': # check if the latter is in the consonent list
        print(f"{Latter} is a consonent") # print if the latter is a consonent
    else:
        print("Invalid input. Please enter a single alphabet letter.") # print if the input is invalid

    # ask the user if they want to continue or not

    cont = input("Do you want to continue? (yes/no): ").lower() # take input from user and convert it to lower case
    if cont != 'yes': # check if the user wants to continue or not
        break # break the loop if the user does not want to continue
