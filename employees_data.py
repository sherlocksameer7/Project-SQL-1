import sqlite3

from prettytable import PrettyTable

connection = sqlite3.connect("company.db") # creating a database

list_of_Tables = connection.execute("Select name from sqlite_master Where type='table' And name='Employees'").fetchall()

if list_of_Tables != []:
    print("Table not found!!! ")

else:

     connection.execute('''   Create Table Employees(
                      EmployeeID Integer Primary Key Autoincrement,
                      EmployeeName Text,
                      EmployeeDesingnation Text,
                      EmployeeSalary Integer,
                      EmployeeCompanyName Text,
                      EmployeeMobileNumber Integer
     );     ''')
     print("Table Created Successfully")

while True:
    print("Select an option from the menu: ?  ")

    print("1. Add an Employee ")
    print("2. View an all Employees ")
    print("3. Search an Employee using Employee Designation ")
    print("4. Search an Employee using Employee ID ")
    print("5. Update an Employee using Employee Name ")
    print("6. Delete an Employee using Employee Designation ")
    print("7. Delete an Employee using Employee Name ")
    print("8. Highest Salary of all of Employees ")
    print("9. Lowest Salary of all of Employees ")
    print("10. Sum of an Employee using Employee Salary ")
    print("11. Count of a total Employee ")
    print("12. Exit ")

    choice = int(input("Enter a choice ? "))

    if choice == 1:
        get_employeeName = input("Enter Employee Name: ")
        get_employeeDesig = input("Enter Employee Designation: ")
        get_employeeSalary = input("Enter Employee Salary: ")
        get_employee_companyName = input("Enter Employee's Company Name: ")
        get_employeeMobile = input("Enter Employee's Mobile No: ")

        connection.execute("Insert Into Employees(EmployeeName, EmployeeDesingnation, EmployeeSalary, EmployeeCompanyName, EmployeeMobileNumber) \
                        Values ('" + get_employeeName + "','" + get_employeeDesig + "'," + get_employeeSalary + ",'" + get_employee_companyName + "'," + get_employeeMobile + ")")
        connection.commit()

        print("Inserted Successfully")

    elif choice == 2:

        result = connection.execute("Select * from Employees")

        table = PrettyTable(["ID", "Employee Name", "Employee Designation", "Employee Salary", "Company Name", "Mobile Number"])

        for i in result:

            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5]])

        print(table)

    elif choice == 3:

        getdesig = input("Enter an Employee Designation to be Searched: ? ")

        result = connection.execute("Select * from Employees Where EmployeeDesingnation like '%"+getdesig+"%'")

        table = PrettyTable(["ID", "Employee Name", "Employee Designation", "Employee Salary", "Company Name", "Mobile Number"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5]])

        print(table)

    elif choice == 4:

        get_ID = input("Enter an Employee ID to be Searched: ? ")

        result = connection.execute("Select * from Employees Where EmployeeID= " +get_ID)

        table = PrettyTable(["ID", "Employee Name", "Employee Designation", "Employee Salary", "Company Name", "Mobile Number"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5]])

        print(table)

    elif choice == 5:

        getName = input("Enter an Employee Name to be Updated: ? ")

        get_employeeDesig = input("Enter New Employee Designation: ")
        get_employeeSalary = input("Enter New Employee Salary: ")
        get_employee_companyName = input("Enter New Employee's Company Name: ")
        get_employeeMobile = input("Enter New Employee's Mobile No: ")

        connection.execute("Update Employees \
        Set EmployeeDesingnation= '" + get_employeeDesig + "', EmployeeSalary= " + get_employeeSalary + ",\
        EmployeeCompanyName= '" + get_employee_companyName + "', EmployeeMobileNumber= " + get_employeeMobile + " Where \
        EmployeeName='"+getName+"'")

        connection.commit()

        print("Successfully Updated")

    elif choice == 6:

        get_employeeDesig = input("Enter a Employee Designation to be Deleted? ")

        connection.execute("Delete from Employees Where EmployeeDesingnation= '"+get_employeeDesig+"'")

        connection.commit()

        print("Deleted Successfully")

    elif choice == 7:

        get_employee_Name = input("Enter a Employee Designation to be Deleted? ")

        connection.execute("Delete from Employees Where EmployeeName= '"+get_employee_Name+"'")

        connection.commit()

        print("Deleted Successfully")

    elif choice == 8:

        result = connection.execute("Select * from Employees Where EmployeeSalary= (Select Max(EmployeeSalary) from Employees)")

        table = PrettyTable(["ID", "Employee Name", "Employee Designation", "Employee Salary", "Company Name", "Mobile Number"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5]])

        print(table)

    elif choice == 9:

        result = connection.execute("Select * from Employees Where EmployeeSalary= (Select Min(EmployeeSalary) from Employees)")

        table = PrettyTable(["ID", "Employee Name", "Employee Designation", "Employee Salary", "Company Name", "Mobile Number"])

        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5]])

        print(table)

    elif choice == 10:

        result = connection.execute("Select Sum(EmployeeSalary) as salary from Employees")

        for i in result:

            print("Total sum of Employees by using Name: ", i[0])

    elif choice == 11:

        result = connection.execute("Select Count(*) as count from Employees")

        for i in result:

            print("Total Count of all the items in Employees: ", i[0])

    elif choice == 12:

        connection.close()

        break

    else:

        print("Invalid Choice!  ")