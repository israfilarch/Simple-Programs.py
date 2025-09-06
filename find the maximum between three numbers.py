# find the maximum between three numbers repeatedly

while True:   # infinite loop
    # taking user input
    num1 = int(input("Enter the first number:")) 
    num2 = int(input("Enter the second number:"))
    num3 = int(input("Enter the 3rd number:"))
    
    #print the maximum number using the max () function
    print("The maximum number is :",max(num1,num2,num3)) 
    
    # asking user to do you continue
    choice = input("Do you want to continue (yes/no) :").lower() # lower() function user for capital and small latter parform same input
    
    # if user choice no,exit the loop
    if choice == "no":
        print("Thanks for using this program!")
        break