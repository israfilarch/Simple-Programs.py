# chack eligibility for admission to a professional course

while True: # Loop to allow multiple checks
    
   #taking input from user 
    a = int(input("Enter your math marks: "))

    b = int(input("Enter your physics marks: "))

    c = int(input("Enter your chemistry marks: "))
    
    #checking eligibility
    if a >= 65 and b >= 55 and c >= 50 or (a + b + c) >= 180 or (a + b) >= 140:
        print("You are eligible for admission to the professional course.")
    else:
        print("You are not eligible for admission to the professional course.")
    
    #asking user if they want to check again
    choice = input("Do you want to check again? (yes/no): ").lower() # lower use for case insensitive comparison
    if choice != 'yes': # when user input is not yes then break the loop
        break

