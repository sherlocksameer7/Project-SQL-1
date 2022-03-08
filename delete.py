import sqlite3

connection = sqlite3.connect("company.db")

get_employee = input("Enter a EmployeeID to be Deleted? ")

connection.execute("Delete from Employees Where EmployeeID=" +get_employee)

connection.commit()

print("Deleted Successfully")

result = connection.execute("Select * From Employees")

for i in result:
    print("EmployeeID", i[0])
    print("EmployeeName", i[1])
    print("EmployeeDesingnation", i[2])
    print("EmployeeSalary", i[3])
    print("EmployeeCompanyName", i[4])
    print("EmployeeMobileNumber", i[5])