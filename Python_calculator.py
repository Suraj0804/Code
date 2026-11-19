def Calculator():
    print(Calculator)
    print("1. Add")
    print("2. sub")
    print("3. mul")
    print("4. div")
    
    
    choice = input("Enter your choice (1-4):")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == "1":
        print("Result:", num1 + num2)
    elif choice == "2":
        print("Result:", num1 - num2)
    elif choice == "3":
        print("Result", num1 * num2)
    elif choice == "4":
        if num2 !=0:
            print("Result:", num1/num2)
        else:
            print("Error! cannot divide by zero.")
    else:
        print("Invalid Choice!")
        
Calculator()