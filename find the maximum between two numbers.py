# Program to find the maximum between two numbers repeatedly

while True:   # infinite loop
    # taking input from user
    a = int(input("Enter your 1st number: "))   # user er 1st number input
    b = int(input("Enter your 2nd number: "))   # user er 2nd number input

    # printing the maximum using max() function
    print("Maximum number is:", max(a, b))  

    # asking user if he/she wants to continue
    choice = input("Do you want to continue? (yes/no): ")   
    
    if choice.lower() != "yes":   # when user choice no break the loop
        print("Thanks for using this program!")  
        break   # exit the loop