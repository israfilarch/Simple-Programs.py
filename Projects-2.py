# 🧮 Arithmetic Operator Calculator
# এই প্রোগ্রাম দিয়ে তুমি দুটি সংখ্যার উপর চারটি অপারেশন করতে পারবে:
# Addition (যোগ), Subtraction (বিয়োগ), Multiplication (গুণ), Division (ভাগ)

while True:  # এই লুপের কারণে প্রোগ্রাম ইউজার চাইলে বারবার চলবে
    # মেনু দেখানো হচ্ছে
    print("Select an operation to perform:\n" \
          "1. Addition\n" \
          "2. Subtraction\n" \
          "3. Multiplication\n" \
          "4. Division")

    # ইউজারকে অপারেশন বেছে নিতে বলা হচ্ছে
    choice = input("Enter choice (1/2/3/4): ")

    # দুটি সংখ্যা ইনপুট নেয়া হচ্ছে
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    # নির্বাচিত অপারেশন চেক করে রেজাল্ট দেখানো হচ্ছে
    if choice == '1':  # যদি ইউজার 1 চয়েস করে, তাহলে দুইটি সংখ্যার যোগফল দেখানো হবে |
        print("Result:", a + b)  # যোগ
    elif choice == '2':  # যদি ইউজার 2 চয়েস করে, তাহলে দুইটি সংখ্যার বিয়োগফল দেখানো হবে |
        print("Result:", a - b)  # বিয়োগ
    elif choice == '3': # যদি ইউজার 3 চয়েস করে, তাহলে দুইটি সংখ্যার গুণফল দেখানো হবে |
        print("Result:", a * b)  # গুণ
    elif choice == '4':  # যদি ইউজার 4 চয়েস করে, তাহলে দুইটি সংখ্যার ভাগফল দেখানো হবে |
        if b and a == 0:  # ভাগ করার আগে divisor (b and a) শূন্য কি না সেটা চেক করা হচ্ছে
            print("Error: Division by zero is not allowed.")
        else:
            print("Result:", a / b)  # ভাগ
    else:
        print("Invalid input. Please select 1/2/3/4.")

    # ইউজারকে জিজ্ঞেস করা হচ্ছে আবার গণনা করবে কিনা
    next_calculation = input("Do you want to perform another calculation? (yes/no): ") 
    if next_calculation.lower() != 'yes': # ইউজারের input নাও এবং সব character কে lowercase এ রূপান্তর করো 
        # এর ফলে 'Yes', 'YES', 'yEs' যেকোনোভাবে typed হোক না কেন সব হয়ে যাবে 'yes'
        print("Thank you for using the calculator! 👋")

        break  # যদি 'yes' না দেয় তাহলে প্রোগ্রাম শেষ হয়ে যাবে
