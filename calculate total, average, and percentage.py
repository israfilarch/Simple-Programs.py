# Program to calculate total, average, and percentage of five subjects

while True:
    # Taking input marks for 5 subjects from the user
    sub1 = float(input("Enter marks of Bangla: "))
    sub2 = float(input("Enter marks of English: "))
    sub3 = float(input("Enter marks of Ict: "))
    sub4 = float(input("Enter marks of Civics: "))
    sub5 = float(input("Enter marks of Social Work: "))

    # Calculating total marks
    total = sub1 + sub2 + sub3 + sub4 + sub5

    # Calculating average marks
    average = total / 5

    # Assuming each subject is out of 100, so maximum marks = 500
    percentage = (total / 500) * 100

    # Printing the results
    print("--- Result ---")
    print("Total Marks:", total)
    print("Average Marks:", average)
    print("Percentage:", percentage, "%")

    # Asking user if they want to continue
    choice = input("Do you want to calculate again? (yes/no): ").lower()

    # If user types 'no', break the loop
    if choice == "no":
        print("Thanks for using this program!")
        break
