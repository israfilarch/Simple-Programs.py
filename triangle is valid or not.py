# check the triangle valid or not for this angle sum of three sides is 180 degree

while True: # infinite loop
    # take input from the user
    a = float(input("Enter the angle of side a: "))
    b = float(input("Enter the angle of side b: "))
    c = float(input("Enter the angle of side c: "))

    # calculate the sum of three sides
    if a + b + c == 180 or (a + b > c and a + c > b and b + c > a):
    
        print("The triangle is valid.")
    
    # when 3 sides are not valid
    elif a + b + c != 180 or (a + b < c or a + c < b or b + c < a):
        print("The triangle is not valid.")
    else:
        print("Invalid input. Please enter valid lengths for the sides of the triangle.")

    # ask the user if they want to continue
    choice = input("Do you want to check another triangle? (yes/no): ") # take input from the user to continue or not

    if choice.lower() != 'yes': # if the user input is not yes then

        break # break the loop
