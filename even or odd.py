# find any code to check if a number is even or odd

while True: # infinite loop
    # take input from the user
    num = int(input("Enter a number: "))

    # check if number is even or odd
    if num % 2 == 0: # if number is divisible by 2
       print(f"The number is even :",num)
    else: # if number is not divisible by 2
      print(f"The number is odd :",num)
    
    # ask the user if they want to check another number
    choice = input("Do you want to check another number? (yes/no): ")
    if choice.lower() != 'yes': # if user does not want to check another number
        break # exit the loop