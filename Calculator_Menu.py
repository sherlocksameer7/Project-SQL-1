while True:
    print("Select an option from the Menu to perform an Operation ? ")
    print("1. Add 2 Numbers ")
    print("2. Sub 2 Numbers ")
    print("3. Mul 2 Numbers ")
    print("4. Div 2 Numbers ")
    print("5. Exit ")

    choice = int(input("Enter a Choice ? "))  # to get a choice using creation of new variable.

    if choice == 1:
        x = int(input("Enter 1st Number "))
        y = int(input("Enter 2nd Number"))
        z = x + y
        print(z)

    elif choice == 2:
        x = int(input("Enter 1st Number "))
        y = int(input("Enter 2nd Number"))
        z = x - y
        print(z)

    elif choice == 3:
        x = int(input("Enter 1st Number "))
        y = int(input("Enter 2nd Number"))
        z = x * y
        print(z)

    elif choice == 4:
        x = int(input("Enter 1st Number "))
        y = int(input("Enter 2nd Number"))
        z = x / y
        print(z)

    elif choice == 5:
        break

    else:
        print("Invalid Choice to perform an Operation ??? ")