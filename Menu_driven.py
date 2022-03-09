while True:
    print("Select an option from the Menu ? ")
    print("1. Add an Employee ")
    print("2. Search an Employee ")
    print("3. Update an Employee ")
    print("4. Delete an Employee ")
    print("5. Exit ")

    choice = int(input("Enter a Choice ? "))

    if choice == 1:
        print("Selected an Option to Enter/Add an Employee Data")

    elif choice == 2:
        print("Selected an Option to Search an Employee Data")

    elif choice == 3:
        print("Selected an Option to Update an Employee Data")

    elif choice == 4:
        print("Selected an Option to Delete an Employee Data")

    elif choice == 5:
        break

    else:
        print("Invalid Choice ??? ")