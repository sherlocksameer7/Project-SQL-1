import sqlite3

connection = sqlite3.connect("company.db")

get_employee = input("Enter a EmployeeID to be Searched? ")

result = connection.execute("Select * From Employees Where EmployeeID=" +get_employee)

for i in result:
    print("EmployeeID", i[0])
    print("EmployeeName", i[1])
    print("EmployeeDesingnation", i[2])
    print("EmployeeSalary", i[3])
    print("EmployeeCompanyName", i[4])
    print("EmployeeMobileNumber", i[5])

