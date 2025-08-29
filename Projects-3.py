# Program to calculate the area of a rectangle

while True:
  a = float(input("Enter the length of the rectangle: "))   # takes rectangle length as float input
  b = float(input("Enter the breadth of the rectangle: "))  # takes rectangle breadth as float input

  area = a * b   # calculates area by multiplying length and breadth


  print("The area of the rectangle is:", area)   # prints the calculated area

  again = str(input("Do you want again ,(yes/no): "))  # asks user if they want to run the program again
  again.lower()   # converts user input to lowercase to handle case sensitivity
  if again == 'no':   # if user input is  'no', break the loop and end the program
        print("Thank you for using the program!") #Thank you for using the program
        break
  
